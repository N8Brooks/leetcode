class TimeLimitedCache {
  constructor() {
    this.cache = new Map();
  }

  /**
   * @param {number} key
   * @param {number} value
   * @param {number} time until expiration in ms
   * @return {boolean} if un-expired key already existed
   */
  set(key, value, duration) {
    const exists = this.clear(key);
    const id = setTimeout(this.delete, duration, key);
    this.cache.set(key, { value, id });
    return exists;
  }

  /**
   * @param {number} key
   * @return {boolean} if un-expired key already existed
   */
  clear(key) {
    const entry = this.cache.get(key);
    if (entry) {
      clearTimeout(entry.id);
      return true;
    }
    return false;
  }

  /**
   * @param {number} key
   */
  delete = (key) => {
    this.cache.delete(key);
  };

  /**
   * @param {number} key
   * @return {number} value associated with key
   */
  get(key) {
    return this.cache.get(key)?.value ?? -1;
  }

  /**
   * @return {number} count of non-expired keys
   */
  count() {
    return this.cache.size;
  }
}

jest.useFakeTimers();

it("Case 1", () => {
  // 0 TimeLimitedCache
  const cache = new TimeLimitedCache();
  // 0 set 1 42 100
  expect(cache.set(1, 42, 100)).toBe(false);
  // 50 get 1
  jest.advanceTimersByTime(50);
  expect(cache.get(1)).toBe(42);
  // 50 count
  expect(cache.count()).toBe(1);
  // 150 get 1
  jest.advanceTimersByTime(100);
  expect(cache.get(1)).toBe(-1);
});

it("Case 2", () => {
  // 0 TimeLimitedCache
  const cache = new TimeLimitedCache();
  // 0 set 1 42 50
  expect(cache.set(1, 42, 50)).toBe(false);
  // 40 set 1 50 100
  jest.advanceTimersByTime(40);
  expect(cache.set(1, 50, 100)).toBe(true);
  // 50 get 1
  jest.advanceTimersByTime(10);
  expect(cache.get(1)).toBe(50);
  // 120 get 1
  jest.advanceTimersByTime(70);
  expect(cache.get(1)).toBe(50);
  // 200 get 1
  jest.advanceTimersByTime(80);
  expect(cache.get(1)).toBe(-1);
  // 250 count
  expect(cache.count()).toBe(0);
});
