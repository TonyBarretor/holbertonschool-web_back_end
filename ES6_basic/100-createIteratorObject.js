export default function createIteratorObject(report) {
  function* iterateEmployees(report) {
    for (const department in report.allEmployees) {
      // eslint-disable-next-line no-prototype-builtins
      if (report.allEmployees.hasOwnProperty(department)) {
        const employees = report.allEmployees[department];
        for (const employee of employees) {
          yield employee;
        }
      }
    }
  }

  return {
    [Symbol.iterator]() {
      return iterateEmployees(report);
    },
  };
}
