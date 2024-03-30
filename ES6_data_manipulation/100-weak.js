// 100-weak.js

// Export a const instance of WeakMap and name it weakMap
export const weakMap = new WeakMap();

// Export a new function named queryAPI
export function queryAPI(endpoint) {
  // Track within the weakMap the number of times queryAPI is called for each endpoint.
  // Check if the endpoint exists in the weakMap, if not initialize its count to 0
  if (!weakMap.has(endpoint)) {
    weakMap.set(endpoint, 0);
  }

  // Increment the count for the endpoint
  const count = weakMap.get(endpoint) + 1;
  weakMap.set(endpoint, count);

  // When the number of queries is >= 5 throw an error with the message Endpoint load is high
  if (count >= 5) {
    throw new Error('Endpoint load is high');
  }
}

