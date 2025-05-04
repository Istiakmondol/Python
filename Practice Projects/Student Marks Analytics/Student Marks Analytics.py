students = [
    ("John", 78, 85, 90),
    ("Alice", 92, 88, 79),
    ("Bob", 65, 70, 60),
    ("Daisy", 80, 75, 85),
    ("Charlie", 95, 100, 98),
    ("Eve", 58, 60, 55),
    ("Frank", 72, 68, 80),
    ("Grace", 85, 90, 92),
]

def stuent_names (students):
    student_list=[]
    for i in students:
        student_list.append(i[0])
    print(f"Student Names: {student_list}")

def highest_mark_student (students):
    marks=0
    for i in students:
        total=sum(i[1:])
        if marks<total:
            marks=total
            name=i[0]
    print(f"Highest Total Scorer: {name} with total {marks}")

def above_90_list (students):
    lst=[]
    for i in students:
        if i[1]>90 or i[2]>90 or i[3]>90:
            lst.append(i[0])
    lst.sort()
    print(f"Top Scorers (90+ in any subject): {lst}")

def check_name (students):
    name=input("Enter Student name: ")
    for i in students:
        if name in i:
            print(f"Is {name} in the dataset?: YES")
            break
    else:
        print(f"Is {name} in the dataset?: NO")

def dict_sname_value (students):
    dict={}
    for i in students:
        total=sum(i[1:])
        dict[i[0]]=total/3
    print("Average Score per Student: ")
    for i in dict.items():
        print(i)
    
def high_avg_scr (students):
    high=0
    for i in students:
        total=sum(i[1:])
        marks=total/3
        if(high<marks):
            high=marks
            name=i[0]
    print(f"Top Average Scorer: {name} with average {high}")

def bonus_one (students):
    dict1={}
    for i in students:
        total=sum(i[1:])
        dict1[i[0]]=total/3
    sorted_avg = sorted(dict1.items(), key=lambda x: x[1],reverse=True)
    print("\nStudents sorted by Average Score (Highest to Lowest):")
    for name, avg in sorted_avg:
        print(f"{name}: {avg:.2f}")

def pass_fail (students):
    res={}
    for i in students:
        total=sum(i[1:])
        marks=total/3
        if(marks>=60):
            res[i[0]]="Pass"
        else:
            res[i[0]]="Fail"
    print("Pass / Fail Status (Pass if Average >= 60):")
    for name,status in res.items():
        print(f"{name}: {status}")

def main():
    print("Student Marks Analytics")
    while(True):
        print("1. Print all student names")
        print("2. Find the student with the highest total marks")
        print("3. students who scored above 90 in any subject (top scorers)")
        print("4. Check if a student is in the dataset")
        print("5. Create a dictionary with keys & values")
        print("6. Print the student(s) with the highest average score")
        print("7. Exit")
        print()
        print("**************Bonus**************")
        print("8. BONUS, Sorting by average score (highest to lowest)")
        print("9. Pass or Fail according to their marks")
        choice=int(input("Enter your Choice: "))

        if choice==1:
            stuent_names (students)
        elif choice==2:
            highest_mark_student (students)
        elif choice==3:
            above_90_list (students)
        elif choice==4:
            check_name (students)
        elif choice==5:
            dict_sname_value (students)
        elif choice==6:
            high_avg_scr (students)
        elif choice==8:
            bonus_one (students)
        elif choice==9:
            pass_fail (students)
        elif choice==7:
            break
        else:
            print("Enter a valid number")

if __name__ == "__main__":
    main()


