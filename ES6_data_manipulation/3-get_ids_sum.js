export default function getStudentIdsSum(studentsList) {
  const sumStudentsIds = studentsList.reduce(
    (accumulator, currentValue) => accumulator + currentValue.id, 0,
  );
  return sumStudentsIds;
}
