employees = [
    ("John", "HR", 50000),
    ("Alice", "Tech", 75000),
    ("Bob", "Tech", 62000),
    ("Daisy", "HR", 52000),
    ("Charlie", "Sales", 47000),
    ("Eve", "Tech", 88000),
    ("Frank", "Sales", 45000),
    ("Grace", "Tech", 61000),
]

def emp_name (employees):
    print("Employee names are: ")
    for i in employees:
        print(i[0])

def high_salary_emp (employees):
    temp=0
    for i in employees:
        temp_lst=[]
        if i[2]>temp:
            #temp_lst.clear()
            temp=i[2]
            temp_lst.append(i)
            res=temp_lst.pop()
    print("High salary emp details: ",res)

def unique_dept (employees):
    uniq_dept_set=set()
    for i in employees:
        uniq_dept_set.add(i[1])
    print(uniq_dept_set)

def find_dept (employees):
    dept_name=input("Enter the dept name you are looking: ")
    dept_name=dept_name.title()
    for i in employees:
        if dept_name in i:
            print("Name Present in the dataset")
            break
    else:
            print("Name not Present in dataset...")

def create_dic (employees):
    dic_of_emp={}
    for name,dept,salary in employees:
        if dept not in dic_of_emp:
            dic_of_emp[dept]=[]
        dic_of_emp[dept].append(name)
    print("Department-wise Employees: ")
    for i in dic_of_emp.items():
        print(i)

def avg_salary (employees):
    avg_dic={}
    for i in employees:
        avg=0
        flag=0
        if i[1] in avg_dic:
            continue
        else:
            for j in employees:
                if i[1]==j[1]:
                    avg=avg+j[2]
                    flag=flag+1
            avg=avg/flag
            avg_dic[i[1]]=avg
        ##print(f"Avg Salary of {i[1]} is: {avg}")
        ##employees.remove(i)
    print("average salary for each department: ")
    for i in avg_dic.items():
        print(i)

def main():
    print("Employee Data Analysis")
    while(True):
        print("1. list of all employee names")
        print("2. employee with the highest salary and  details")
        print("3. set of all unique departments")
        print("4. Check if the department exists in the dataset")
        print("5. Create a dictionary with keys & values")
        print("6. Calculate and print the average salary for each department")
        print("7. Exit")
        x=int(input("Enter your operation: "))

        if x==1:
            emp_name (employees)
        elif x==2:
            high_salary_emp (employees)
        elif x==3:
            unique_dept (employees)
        elif x==4:
            find_dept (employees)
        elif x==5:
            create_dic (employees)
        elif x==6:
            avg_salary (employees)
        elif x==7:
            break
        else:
            print("Enter a valid number")
if __name__ == "__main__":
    main()
    


