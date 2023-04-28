/**
 * @param {any} object
 * @return {string}
 */
function jsonStringify(object) {
  switch (typeof object) {
    case "number":
    case "boolean":
      return `${object}`;
    case "string":
      return `"${object}"`;
    default:
      return object === null
        ? "null"
        : Array.isArray(object)
          ? `[${object.map(jsonStringify)}]`
          : `{${Object.entries(object).map(
            ([key, val]) => `"${key}":${jsonStringify(val)}`
          )}}`;
  }
}

it("Case 1", () => {
  expect(jsonStringify({ y: 1, x: 2 })).toBe('{"y":1,"x":2}');
});

it("Case 2", () => {
  expect(jsonStringify({ a: "str", b: -12, c: true, d: null })).toBe(
    '{"a":"str","b":-12,"c":true,"d":null}'
  );
});

it("Case 3", () => {
  expect(jsonStringify({ key: { a: 1, b: [{}, null, "Hello"] } })).toBe(
    '{"key":{"a":1,"b":[{},null,"Hello"]}}'
  );
});

it("Case 4", () => {
  expect(jsonStringify(true)).toBe("true");
});
