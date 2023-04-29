/**
 * @param {Array} arr
 * @return {Generator}
 */
function* inorderTraversal(arr) {
  yield* arr.flat(Infinity);
}

it("Case 1", () => {
  expect([...inorderTraversal([[[6]], [1, 3], []])]).toEqual([6, 1, 3]);
});

it("Case 2", () => {
  expect([...inorderTraversal([])]).toEqual([]);
});
