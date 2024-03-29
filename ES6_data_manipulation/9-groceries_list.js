export default function groceriesList() {
  const groceriesObj = {
    Apples: 10,
    Tomatoes: 10,
    Pasta: 1,
    Rice: 1,
    Banana: 5,
  };

  const groceriesMap = new Map();
  for (const [k, v] of Object.entries(groceriesObj)) {
    groceriesMap.set(k, v);
  }

  return groceriesMap;
}
