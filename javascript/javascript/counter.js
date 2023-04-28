/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
  return () => n++;
};

it("Case 1", () => {
  const counter = createCounter(10);
  expect(Array.from({ length: 3 }, counter)).toEqual([10, 11, 12]);
});

it("Case 2", () => {
  const counter = createCounter(-2);
  expect(Array.from({ length: 5 }, counter)).toEqual([-2, -1, 0, 1, 2]);
});
