import csv
import os
def load_students(filename):
        with open (filename,"r")as f:
            n=csv.DictReader(f)  
            return(list(n))
# a=load_students("students.csv")                 
# print(a)

def save_students(filename, students):
    if len(students) > 0:
        keys = students[0].keys()
        with open(filename, "w")as w:
            writer = csv.DictWriter(w, fieldnames=keys)
            writer.writeheader()
            writer.writerows(students)
# my_students = load_students("students.csv")
# save_students("students_test.csv", my_students)

def add_student(students, name, grade, class_name):
    addi_student={name:"name",grade:"grade",class_name:"class_name"}
    students.append(addi_student)
# טעינת התלמידים הקיימים
my_students = load_students("students.csv")

# הדפסת כמות התלמידים לפני ההוספה
print("Before:", len(my_students))

# קריאה לפונקציה להוספת תלמיד חדש
add_student(my_students, "דוד לוי", "90", "ג1")

# הדפסת כמות התלמידים אחרי ההוספה (המספר אמור לגדול ב-1)
print("After:", len(my_students))

