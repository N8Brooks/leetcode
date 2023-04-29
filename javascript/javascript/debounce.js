/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
function debounce(fn, t) {
  let id = NaN;
  return (...args) => {
    clearTimeout(id);
    id = setTimeout(() => fn(...args), t);
  };
}

jest.useFakeTimers();

it("Case 1", () => {
  const fn = jest.fn();
  const debouncedFn = debounce(fn, 50);

  jest.advanceTimersByTime(50);
  debouncedFn(1);

  jest.advanceTimersByTime(25);
  debouncedFn(2);

  jest.advanceTimersByTime(50);
  expect(fn).toHaveBeenNthCalledWith(1, 2);
});

it("Case 2", () => {
  const fn = jest.fn();
  const debouncedFn = debounce(fn, 20);

  jest.advanceTimersByTime(50);
  debouncedFn(1);
  jest.advanceTimersByTime(20);
  expect(fn).toHaveBeenNthCalledWith(1, 1);

  jest.advanceTimersByTime(30);
  debouncedFn(2);
  jest.advanceTimersByTime(20);
  expect(fn).toHaveBeenNthCalledWith(2, 2);
});

it("Case 2", () => {
  const fn = jest.fn();
  const debouncedFn = debounce(fn, 150);

  jest.advanceTimersByTime(50);
  debouncedFn(1, 2);
  jest.advanceTimersByTime(150);
  expect(fn).toHaveBeenNthCalledWith(1, 1, 2);

  jest.advanceTimersByTime(100);
  debouncedFn(3, 4);
  debouncedFn(5, 6);

  jest.advanceTimersByTime(150);
  expect(fn).toHaveBeenNthCalledWith(2, 5, 6);
});
