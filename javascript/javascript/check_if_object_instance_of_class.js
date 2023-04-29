/**
 * @param {any} object
 * @param {any} classFunction
 * @return {boolean}
 */
function checkIfInstanceOf(obj, classFunction) {
  while (obj !== null && obj !== undefined) {
    if (obj.constructor === classFunction) {
      return true;
    }
    obj = Object.getPrototypeOf(obj);
  }
  return false;
}

it("Case 1", () => {
  expect(checkIfInstanceOf(new Date(), Date)).toBe(true);
});

it("Case 2", () => {
  class Animal { }
  class Dog extends Animal { }
  expect(checkIfInstanceOf(new Dog(), Animal)).toBe(true);
});

it("Case 3", () => {
  expect(checkIfInstanceOf(Date, Date)).toBe(false);
});

it("Case 4", () => {
  expect(checkIfInstanceOf(5, Number)).toBe(true);
});

it("Case undefined, null", () => {
  expect(checkIfInstanceOf(undefined, null)).toBe(false);
});
