/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
function reduce(nums, fn, init) {
  for (const num of nums) {
    init = fn(init, num);
  }
  return init;
}

it("Case 1", () => {
  expect(reduce([1, 2, 3, 4], (accum, curr) => accum + curr, 0)).toBe(10);
});

it("Case 2", () => {
  expect(reduce([1, 2, 3, 4], (accum, curr) => accum + curr * curr, 100)).toBe(
    130
  );
});

it("Case 3", () => {
  expect(reduce([], (accum, curr) => accum + curr, 25)).toBe(25);
});
