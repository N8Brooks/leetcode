/**
 * @param {Function[]} functions
 * @return {Function}
 */
function compose(functions) {
  return (init) => functions.reduceRight((val, func) => func(val), init);
}

it("Case 1", () => {
  const func = compose([(x) => x + 1, (x) => x * x, (x) => 2 * x]);
  expect(func(4)).toBe(65);
});

it("Case 2", () => {
  const func = compose([(x) => 10 * x, (x) => 10 * x, (x) => 10 * x]);
  expect(func(1)).toBe(1000);
});

it("Case 3", () => {
  const func = compose([]);
  expect(func(42)).toBe(42);
});
