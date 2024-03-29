export default function updateStudentGradeByCity(studentsList, city, newGrades) {
  const filteredStudents = studentsList.filter((student) => student.location === city);

  const newStudentGrades = filteredStudents.map((student) => {
    const matchNewGrade = newGrades.find(({ studentId }) => studentId === student.id);

    const updatedGrade = matchNewGrade ? matchNewGrade.grade : 'N/A';

    return { ...student, grade: updatedGrade };
  });

  return newStudentGrades;
}
