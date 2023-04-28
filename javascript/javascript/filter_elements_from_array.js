/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
function filter(arr, fn) {
  return arr.flatMap((val, i) => (fn(val, i) ? [val] : []));
}

it("Case 1", () => {
  expect(filter([0, 10, 20, 30], (n) => n > 10)).toEqual([20, 30]);
});

it("Case 2", () => {
  expect(filter([1, 2, 3], (_, i) => i === 0)).toEqual([1]);
});

it("Case 3", () => {
  expect(filter([-2, -1, 0, 1, 2], (n) => n + 1)).toEqual([-2, 0, 1, 2]);
});
