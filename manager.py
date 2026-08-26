import csv
import os
###1
def load_students(filename):
        with open (filename,"r")as f:
            n=csv.DictReader(f)  
            return(list(n))
# a=load_students("students.csv")                 
# print(a)
###2
def save_students(filename, students):
    if len(students) > 0:
        keys = students[0].keys()
        with open(filename, "w")as w:
            writer = csv.DictWriter(w, fieldnames=keys)
            writer.writeheader()
            writer.writerows(students)
# my_students = load_students("students.csv")
# save_students("students_test.csv", my_students)
###3
def add_student(students, name, grade, class_name):
    addi_student={"name":name,"grade":grade,"class":class_name}
    students.append(addi_student)
###4
def find_student(students, name):
    for row in students:
        if row["name"]==name:
            return row
    return None
###5
def class_average(students, class_name):
    total=0
    sumi=0
    sum_class=0
    for i in students:
        if i["class"]==class_name:
            sumi+=int (i["grade"])
            total+=1
            return sum_class
        if sumi==0:
            return 0
        return sumi/total

###6
def top_student(students):
    top_grade = 0
    top_name = None
    for i in students:
        grade=int (i["grade"])
        if grade>top_grade:
            top_grade = grade
            top_name = i ["name"]
    return top_name
        # if top_grade ==0:
    #         return None
    # return students["name"]

###7
def print_all(students):
    print (students)


def main():
    file_name = r"C:\Users\נעמה כהן\Desktop\python_projects\efraim-python\Working with files\students.csv"                   
    students=load_students(file_name)
    while True:
        print("1 :Show all")
        print("2: Add student")
        print("3: Search student")
        print("4: Class average")
        print("5: Top student")
        print("6: Save and exit")

        choice=input("Enter a choice (1-6):")
        if choice=="1":
            print_all(students)
        elif choice == "2":
            name = input("Enter name: ")
            grade = input("Enter grade: ")
            class_name = input("Enter class: ")
            add_student(students, name, grade, class_name)
            save_students(file_name, students)

        elif choice == "3":
            name = input("Enter name to find: ")
            print(find_student(students, name))

        elif choice == "4":
            c = input("Enter class: ")
            print(class_average(students, c))

        elif choice == "5":
            print (top_student(students))
            
            
        elif choice == "6":
            save_students(file_name,students)
            print("Saved successfully")
            break
            
        else:
            print("Invalid selection, try again.")
        print("----------------------------------")

main()
        






