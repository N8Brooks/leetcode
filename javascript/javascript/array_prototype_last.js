Array.prototype.last = function() {
  return this.length ? this[this.length - 1] : -1;
};

it("Case 1", () => {
  expect([1, 2, 3].last()).toBe(3);
});

it("Case 2", () => {
  expect([].last()).toBe(-1);
});
