/**
 * @param {number} rowsCount
 * @param {number} colsCount
 * @return {Array<Array<number>>}
 */
Array.prototype.snail = function(rowsCount, colsCount) {
  if (rowsCount * colsCount !== this.length) {
    return [];
  }
  return Array.from({ length: rowsCount }, (_, row) =>
    Array.from({ length: colsCount }, (_, col) => {
      const i = col * rowsCount;
      const j = col & 1 ? rowsCount - row - 1 : row;
      return this[i + j];
    })
  );
};

it("Case 1", () => {
  expect(
    [
      19, 10, 3, 7, 9, 8, 5, 2, 1, 17, 16, 14, 12, 18, 6, 13, 11, 20, 4, 15,
    ].snail(5, 4)
  ).toEqual([
    [19, 17, 16, 15],
    [10, 1, 14, 4],
    [3, 2, 12, 20],
    [7, 5, 18, 11],
    [9, 8, 6, 13],
  ]);
});

it("Case 2", () => {
  expect([1, 2, 3, 4].snail(1, 4)).toEqual([[1, 2, 3, 4]]);
});

it("Case 2", () => {
  expect([1, 3].snail(2, 2)).toEqual([]);
});
