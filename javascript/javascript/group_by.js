/**
 * @param {Function} fn
 * @return {Array}
 */
Array.prototype.groupBy = function(fn) {
  const cache = Object.create(null);
  for (const elem of this) {
    const key = fn(elem);
    const arr = (cache[key] ??= []);
    arr.push(elem);
  }
  return cache;
};

it("Case 1", () => {
  expect(
    [{ id: "1" }, { id: "1" }, { id: "2" }].groupBy((item) => item.id)
  ).toEqual({
    1: [{ id: "1" }, { id: "1" }],
    2: [{ id: "2" }],
  });
});

it("Case 2", () => {
  expect(
    [
      [1, 2, 3],
      [1, 3, 5],
      [1, 5, 9],
    ].groupBy((list) => String(list[0]))
  ).toEqual({
    1: [
      [1, 2, 3],
      [1, 3, 5],
      [1, 5, 9],
    ],
  });
});

it("Case 3", () => {
  expect([1, 2, 3, 4, 5, 6, 7, 8, 9, 10].groupBy((n) => String(n > 5))).toEqual(
    {
      true: [6, 7, 8, 9, 10],
      false: [1, 2, 3, 4, 5],
    }
  );
});
