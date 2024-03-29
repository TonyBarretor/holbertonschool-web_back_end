export default function updateUniqueItems(mapObj) {
  if (!(mapObj instanceof Map)) {
    throw new Error('Cannot process');
  }

  for (const [key, value] of mapObj.entries()) {
    const updatedValue = value === 1 ? 100 : value;
    mapObj.set(key, updatedValue);
  }

  return mapObj;
}
