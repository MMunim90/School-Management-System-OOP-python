from school import School
from person import Student, Teacher
from subject import Subject
from classroom import ClassRoom

school = School("WUB", "Dhaka")

# Adding Classroom
eight = ClassRoom("Eight")
nine = ClassRoom("Nine")
ten = ClassRoom("Ten")

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

# adding student
rahim = Student("Rahim", eight)
karim = Student("karim", nine)
fahim = Student("Fahim", nine)
rakib = Student("Rakib", ten)
sakib = Student("Sakib", ten)


school.student_addmission(rahim)
school.student_addmission(karim)
school.student_addmission(fahim)
school.student_addmission(rakib)
school.student_addmission(sakib)


# Adding teachers
abul = Teacher("Abul Khan")
babul = Teacher("Babul Khan")
kabul = Teacher("Kabul Khan")

# Adding Subjects
bangla = Subject("Bangla", abul)
physics = Subject("Physics", babul)
chemistry = Subject("Chemistry", babul)
math = Subject("Math", kabul)
ict = Subject("ICT", kabul)

eight.add_subject(bangla)
eight.add_subject(math)
nine.add_subject(math)
nine.add_subject(physics)
nine.add_subject(chemistry)
nine.add_subject(ict)
ten.add_subject(math)
ten.add_subject(physics)
ten.add_subject(chemistry)
ten.add_subject(ict)

eight.take_semester_final_exam()
nine.take_semester_final_exam()
ten.take_semester_final_exam()
print(school)