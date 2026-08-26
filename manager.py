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
    addi_student={"name":name,"grade":grade,"class_name":class_name}
    students.append(addi_student)
###4
def find_student(students, name):
    for row in students:
        if row["name"]==name:
            return row
        else:
           return None
###5
def class_average(students, class_name):
    total=0
    sumi=0
    sum_class=0
    for i in students:
        if students["class"]==class_name:
            total+=1
            sumi+=int (i["grade"])
            sum_class=sumi//total
            return sum_class
        else:
            return 0

###6
def top_student(students):
    sumi=0
    for i in students:
        if students["grade"]>sumi:
            sumi=int (i["grade"])
        if sumi ==0:
            return None
        return students["name"]

###7
def print_all(students):
    for i in students:
        print (i["name"])


def main():
    file_name =r"C:\Users\נעמה כהן\Desktop\python_projects\efraim-python\Working with files\students.csv"
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
            add_student(students)
            save_students(students)
        elif choice == "3":
            find_student(students)
        elif choice == "4":
            class_average(students)
            save_students(students)
        elif choice == "5":
            top_student(students)
            save_students(students)
        elif choice == "6":
            print_all(students)
            save_students(students)
        else:
            if choice >"6" or choice < "0":
                break
        
# if __name__ =="__main__":
#      main()  

main()
        






