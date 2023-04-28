/**
 * @param {any} o1
 * @param {any} o2
 * @return {boolean}
 */
var areDeeplyEqual = function(o1, o2) {
  if (typeof o1 !== "object" || typeof o2 !== "object") {
    return o1 === o2;
  }
  if (Array.isArray(o1) !== Array.isArray(o2)) {
    return false;
  }
  return Object.keys({ ...o1, ...o2 }).every((key) =>
    areDeeplyEqual(o1[key], o2[key])
  );
};

it("Case 1", () => {
  expect(areDeeplyEqual({ x: 1, y: 2 }, { x: 1, y: 2 })).toBe(true);
});

it("Case 2", () => {
  expect(areDeeplyEqual({ y: 2, x: 1 }, { x: 1, y: 2 })).toBe(true);
});

it("Case 3", () => {
  expect(
    areDeeplyEqual({ x: null, L: [1, 2, 3] }, { x: null, L: ["1", "2", "3"] })
  ).toBe(false);
});

it("Case 4", () => {
  expect(areDeeplyEqual(true, false)).toBe(false);
});
