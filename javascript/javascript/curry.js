/**
 * @param {Function} fn
 * @return {Function}
 */
function curry(fn) {
  const args = [];
  return function curried(...rest) {
    args.push(...rest);
    return args.length >= fn.length ? fn(...args) : curried;
  };
}

it("Case 1", () => {
  const func = curry((a, b, c) => a + b + c);
  expect(func(1)(2)(3)).toBe(6);
});

it("Case 2", () => {
  const func = curry((a, b, c) => a + b + c);
  expect(func(1, 2)(3)).toBe(6);
});

it("Case 3", () => {
  const func = curry((a, b, c) => a + b + c);
  expect(func()()(1, 2, 3)).toBe(6);
});

it("Case 4", () => {
  const func = curry(() => 42);
  expect(func()).toBe(42);
});
