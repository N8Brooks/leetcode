/**
 * @param {number} millis
 */
async function sleep(millis) {
  await new Promise((res) => setTimeout(res, millis));
}

jest.useFakeTimers();

it("Case 1", async () => {
  const callback = jest.fn();
  const promise = sleep(100);
  jest.advanceTimersByTime(100);
  await promise.then(callback);
  expect(callback).toHaveBeenCalled();
});

it("Case 2", async () => {
  const callback = jest.fn();
  const promise = sleep(200);
  jest.advanceTimersByTime(200);
  await promise.then(callback);
  expect(callback).toHaveBeenCalled();
});
