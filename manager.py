import csv
import os
def load_students(filename):
        with open (filename,"r")as f:
            n=csv.DictReader(f)  
            return(list(n))
        
a=load_students("students.csv")                 
print(a)