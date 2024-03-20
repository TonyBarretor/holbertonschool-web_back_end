export default function createIteratorObject(report) {
    const allEmployees = report.allEmployees;
    const departments = Object.values(allEmployees);
    let currentDepartmentIndex = 0;
    let currentEmployeeIndex = 0;
  
    return {
      next() {
        const currentDepartment = departments[currentDepartmentIndex];
        if (currentEmployeeIndex >= currentDepartment.length) {
          currentEmployeeIndex = 0;
          currentDepartmentIndex++;
        }
  
        if (currentDepartmentIndex >= departments.length) {
          return { done: true };
        }
  
        const employee = currentDepartment[currentEmployeeIndex];
        currentEmployeeIndex++;
  
        return { value: employee, done: false };
      },
      [Symbol.iterator]() {
        return this;
      },
    };
  }
  