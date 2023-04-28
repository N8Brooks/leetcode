const UUKEY = Symbol();

/**
 * @param {Function} fn
 */
function memoize(fn) {
  const _memo = new Map();
  return function(...args) {
    let memo = _memo;
    for (const arg of args) {
      memo = memo.has(arg) ? memo.get(arg) : memo.set(arg, new Map()).get(arg);
    }
    return memo.has(UUKEY)
      ? memo.get(UUKEY)
      : memo.set(UUKEY, fn(...args)).get(UUKEY);
  };
}

it("Case 1", () => {
  let callCount = 0;
  const sum = (a, b) => {
    callCount++;
    return a + b;
  };
  const call = memoize(sum);
  expect(call(2, 2)).toBe(4);
  expect(callCount).toBe(1);
  expect(call(2, 2)).toBe(4);
  expect(callCount).toBe(1);
  expect(call(1, 2)).toBe(3);
  expect(callCount).toBe(2);
});

it("Case 2", () => {
  let callCount = 0;
  const merge = (a, b) => {
    return { ...a, ...b };
  };
  const call = memoize((a, b) => {
    callCount++;
    return merge(a, b);
  });
  expect(call({}, {})).toEqual({});
  expect(callCount).toBe(1);
  expect(call({}, {})).toEqual({});
  expect(callCount).toBe(2);
  expect(call({}, {})).toEqual({});
  expect(callCount).toBe(3);
});

it("Case 3", () => {
  let callCount = 0;
  const merge = (a, b) => {
    return { ...a, ...b };
  };
  const call = memoize((a, b) => {
    callCount++;
    return merge(a, b);
  });
  const o = {};
  expect(call(o, o)).toEqual({});
  expect(callCount).toBe(1);
  expect(call(o, o)).toEqual({});
  expect(callCount).toBe(1);
  expect(call(o, o)).toEqual({});
  expect(callCount).toBe(1);
});
