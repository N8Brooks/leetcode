/**
 * @param {Function} fn
 */
function memoize(fn, memo = {}) {
  return (...args) => (memo[args] ??= fn(...args));
}

it("Case 1", () => {
  let callCount = 0;
  const sum = (a, b) => {
    callCount++;
    return a + b;
  };
  const call = memoize(sum);
  expect(call(2, 2)).toBe(4);
  expect(call(2, 2)).toBe(4);
  expect(callCount).toBe(1);
  expect(call(1, 2)).toBe(3);
  expect(callCount).toBe(2);
});

it("Case 2", () => {
  let callCount = 0;
  const factorial = (n) => {
    return n <= 1 ? 1 : factorial(n - 1) * n;
  };
  const call = memoize((n) => {
    callCount++;
    return factorial(n);
  });
  expect(call(2)).toBe(2);
  expect(call(3)).toBe(6);
  expect(call(2)).toBe(2);
  expect(callCount).toBe(2);
  expect(call(3)).toBe(6);
  expect(callCount).toBe(2);
});

it("Case 3", () => {
  let callCount = 0;
  const fib = (n) => {
    return n <= 1 ? 1 : fib(n - 1) + fib(n - 2);
  };
  const call = memoize((n) => {
    callCount++;
    return fib(n);
  });
  expect(call(5)).toBe(8);
  expect(callCount).toBe(1);
});
