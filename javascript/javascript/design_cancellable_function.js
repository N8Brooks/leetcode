/**
 * @param {Generator} generator
 * @return {[Function, Promise]}
 */
function cancellable(generator) {
  let cancelled = false;
  let done, value;
  return [
    () => void (cancelled = true),
    (async () => {
      while (!done) {
        try {
          ({ done, value } = generator.next(await value));
          if (cancelled) {
            break;
          }
        } catch (error) {
          if (cancelled) {
            break;
          }
          ({ done, value } = generator.throw(error));
        }
      }
      return cancelled ? generator.throw("Cancelled").value : value;
    })(),
  ];
}

jest.useFakeTimers();

it("Case 1", async () => {
  function* generator() {
    return 42;
  }
  const [cancel, promise] = cancellable(generator());
  setTimeout(cancel, 100);
  await expect(promise).resolves.toEqual(42);
});

it("Case 2", async () => {
  const messages = [];
  function* generator() {
    const msg = yield new Promise((res) => res("Hello"));
    messages.push(msg);
    throw `Error: ${msg}`;
  }
  const [, promise] = cancellable(generator());
  await expect(promise).rejects.toEqual("Error: Hello");
  expect(messages).toEqual(["Hello"]);
});

it("Case 3", async () => {
  function* generator() {
    yield new Promise((res) => setTimeout(res, 200));
    return "Success";
  }
  const [cancel, promise] = cancellable(generator());
  setTimeout(cancel, 100);
  jest.advanceTimersByTime(200);
  await expect(promise).rejects.toEqual("Cancelled");
});

it("Case 4", async () => {
  function* generator() {
    let result = 0;
    yield new Promise((res) => setTimeout(res, 100));
    result += yield new Promise((res) => res(1));
    yield new Promise((res) => setTimeout(res, 100));
    result += yield new Promise((res) => res(1));
    return result;
  }
  const [, promise] = cancellable(generator());
  await jest.advanceTimersByTimeAsync(200);
  await expect(promise).resolves.toEqual(2);
});

it("Case 5", async () => {
  function* generator() {
    let result = 0;
    try {
      yield new Promise((res) => setTimeout(res, 100));
      result += yield new Promise((res) => res(1));
      yield new Promise((res) => setTimeout(res, 100));
      result += yield new Promise((res) => res(1));
    } catch (e) {
      return result;
    }
    return result;
  }
  const [cancel, promise] = cancellable(generator());
  setTimeout(cancel, 150);
  await jest.advanceTimersByTimeAsync(200);
  await expect(promise).resolves.toEqual(1);
});

it("Case 6", async () => {
  function* generator() {
    try {
      yield new Promise((_, reject) => reject("Promise Rejected"));
    } catch (e) {
      let a = yield new Promise((resolve) => resolve(2));
      let b = yield new Promise((resolve) => resolve(2));
      return a + b;
    }
  }
  const [, promise] = cancellable(generator());
  await jest.advanceTimersByTimeAsync(0);
  await expect(promise).resolves.toEqual(4);
});
