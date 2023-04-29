/**
 * @param {any[]} arr
 * @param {number} depth
 * @return {any[]}
 */
function flat(arr, n) {
  return n
    ? arr.flatMap((arr) => (Array.isArray(arr) ? flat(arr, n - 1) : arr))
    : arr;
}

it("Case 1", () => {
  expect(
    flat([1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]], 0)
  ).toEqual([1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]);
});

it("Case 2", () => {
  expect(
    flat([1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]], 1)
  ).toEqual([1, 2, 3, 4, 5, 6, 7, 8, [9, 10, 11], 12, 13, 14, 15]);
});

it("Case 1", () => {
  expect(
    flat(
      [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, [9, 10, 11], 12],
        [13, 14, 15],
      ],
      2
    )
  ).toEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]);
});
