export default function createReportObject(employeesList) {
    return {
      allEmployees: employeesList,
      getNumberOfDepartments: function(allEmployees) {
        return Object.keys(allEmployees).length;
      }
    };
  }
  