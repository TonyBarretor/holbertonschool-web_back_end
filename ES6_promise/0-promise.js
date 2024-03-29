export default function getResponseFromAPI() {
  // Simulate an API call with a delay (Could be replace with actual API logic)
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve({ data: 'Successfully retrieved data' });
    }, 1000);
  });
}
