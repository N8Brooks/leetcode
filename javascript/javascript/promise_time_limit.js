/**
 * @param {Function} fn
 * @param {number} t
 * @return {Promise}
 */
function timeLimit(fn, t) {
  return async function(...args) {
    return Promise.race([
      fn(...args),
      new Promise((_, rej) => setTimeout(rej, t, "Time Limit Exceeded")),
    ]);
  };
}

jest.useFakeTimers();

it("Case 1", async () => {
  const promise = timeLimit(async (n) => {
    await new Promise((res) => setTimeout(res, 100));
    return n * n;
  }, 50)(5);
  jest.advanceTimersByTime(100);
  await expect(promise).rejects.toEqual("Time Limit Exceeded");
});

it("Case 2", async () => {
  const promise = timeLimit(async (n) => {
    await new Promise((res) => setTimeout(res, 100));
    return n * n;
  }, 150)(5);
  jest.advanceTimersByTime(100);
  await expect(promise).resolves.toEqual(25);
});

it("Case 3", async () => {
  const promise = timeLimit(async (a, b) => {
    await new Promise((res) => setTimeout(res, 120));
    return a + b;
  }, 150)(5, 10);
  jest.advanceTimersByTime(120);
  await expect(promise).resolves.toEqual(15);
});

it("Case 4", async () => {
  const promise = timeLimit(async () => {
    throw "Error";
  }, 1000)();
  jest.advanceTimersByTime(0);
  await expect(promise).rejects.toEqual("Error");
});
