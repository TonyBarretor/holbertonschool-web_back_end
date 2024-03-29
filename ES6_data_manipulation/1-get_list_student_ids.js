export default function getListStudentIds(studentsList) {
  const idList = [];
  if (studentsList instanceof Array) {
    studentsList.map((student) => idList.push(student.id));
  }

  return idList;
}
