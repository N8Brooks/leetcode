/**
 * @param {Array} arr
 * @return {Generator}
 */
function* inorderTraversal(_arr) {
  for (const arr of _arr) {
    if (Array.isArray(arr)) {
      yield* inorderTraversal(arr);
    } else {
      yield arr;
    }
  }
}

it("Case 1", () => {
  expect([...inorderTraversal([[[6]], [1, 3], []])]).toEqual([6, 1, 3]);
});

it("Case 2", () => {
  expect([...inorderTraversal([])]).toEqual([]);
});
