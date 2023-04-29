/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
  let [a, b] = [0, 1];
  while (true) {
    yield a;
    [a, b] = [b, a + b];
  }
};

it("Case 1", () => {
  const fib = fibGenerator();
  const arr = Array.from({ length: 5 }, () => fib.next().value);
  expect(arr).toEqual([0, 1, 1, 2, 3]);
});

it("Case 2", () => {
  const fib = fibGenerator();
  const arr = Array.from({ length: 0 }, () => fib.next().value);
  expect(arr).toEqual([]);
});
