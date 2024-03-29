// 100-weak.js

// Export a const instance of WeakMap named weakMap
export const weakMap = new WeakMap();

// Export a new function named queryAPI
export function queryAPI(endpoint) {
    // Check if the endpoint exists in the weakMap, if not initialize its count to 0
    if (!weakMap.has(endpoint)) {
        weakMap.set(endpoint, 0);
    }

    // Increment the count for the endpoint
    const count = weakMap.get(endpoint) + 1;
    weakMap.set(endpoint, count);

    // Check if the number of queries is >= 5, if so, throw an error
    if (count >= 5) {
        throw new Error('Endpoint load is high');
    }
}
