/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
function map(arr, fn) {
  return Array.from(arr, fn);
}

it("Case 1", () => {
  expect(map([1, 2, 3], (n) => n + 1)).toEqual([2, 3, 4]);
});

it("Case 2", () => {
  expect(map([1, 2, 3], (n, i) => n + i)).toEqual([1, 3, 5]);
});

it("Case 3", () => {
  expect(map([10, 20, 30], () => 42)).toEqual([42, 42, 42]);
});
