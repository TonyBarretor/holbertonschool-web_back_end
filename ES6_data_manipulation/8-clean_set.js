export default function cleanSet(set, startString) {
  let result = '';
  if (startString && typeof startString === 'string') {
    set.forEach((value) => {
      if (value.startsWith(startString)) {
        result += `${value.slice(startString.length)}-`;
      }
    });

    return result.slice(0, -1);
  }
  return result;
}
