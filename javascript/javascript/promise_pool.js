/**
 * @param {Function[]} functions
 * @param {number} n
 * @return {Function}
 */
async function promisePool(functions, n) {
  let i = 0;
  return Promise.all(
    functions.slice(0, n).map(async () => {
      while (i < functions.length) {
        await functions[i++]();
      }
    })
  );
}

jest.useFakeTimers();

/**
 * @param {number} n
 */
function getAbc(n) {
  const abc = Array(3).fill("queued");
  promisePool(
    [300, 400, 200].map((millis, i) => async () => {
      abc[i] = "pending";
      await new Promise((res) => setTimeout(res, millis));
      abc[i] = "fulfilled";
    }),
    n
  );
  return abc;
}

it("Case 1", async () => {
  const abc = getAbc(2);
  expect(abc).toEqual(["pending", "pending", "queued"]);
  await jest.advanceTimersByTimeAsync(300);
  expect(abc).toEqual(["fulfilled", "pending", "pending"]);
  await jest.advanceTimersByTimeAsync(100);
  expect(abc).toEqual(["fulfilled", "fulfilled", "pending"]);
  await jest.advanceTimersByTimeAsync(100);
  expect(abc).toEqual(["fulfilled", "fulfilled", "fulfilled"]);
});

it("Case 2", async () => {
  const abc = getAbc(5);
  expect(abc).toEqual(["pending", "pending", "pending"]);
  await jest.advanceTimersByTimeAsync(200);
  expect(abc).toEqual(["pending", "pending", "fulfilled"]);
  await jest.advanceTimersByTimeAsync(100);
  expect(abc).toEqual(["fulfilled", "pending", "fulfilled"]);
  await jest.advanceTimersByTimeAsync(100);
  expect(abc).toEqual(["fulfilled", "fulfilled", "fulfilled"]);
});

it("Case 3", async () => {
  const abc = getAbc(1);
  expect(abc).toEqual(["pending", "queued", "queued"]);
  await jest.advanceTimersByTimeAsync(300);
  expect(abc).toEqual(["fulfilled", "pending", "queued"]);
  await jest.advanceTimersByTimeAsync(400);
  expect(abc).toEqual(["fulfilled", "fulfilled", "pending"]);
  await jest.advanceTimersByTimeAsync(200);
  expect(abc).toEqual(["fulfilled", "fulfilled", "fulfilled"]);
});
