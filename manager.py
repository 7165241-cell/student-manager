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
my_students = load_students("students.csv")
save_students("students_test.csv", my_students)



#     for i in students:
#          filename[i]+=students
#          return filename
# b=save_students("filename")
# print(b)