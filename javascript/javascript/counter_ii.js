/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
function createCounter(init) {
  let count = init;
  return {
    increment: () => ++count,
    decrement: () => --count,
    reset: () => (count = init),
  };
}

it("Example 1", () => {
  const counter = createCounter(5);
  expect(counter.increment()).toBe(6);
  expect(counter.reset()).toBe(5);
  expect(counter.decrement()).toBe(4);
});

it("Example 2", () => {
  const counter = createCounter(0);
  expect(counter.increment()).toBe(1);
  expect(counter.increment()).toBe(2);
  expect(counter.decrement()).toBe(1);
  expect(counter.reset()).toBe(0);
  expect(counter.reset()).toBe(0);
});
