student_list= []

def add_student (student_list) : ## Function for adding students to the list 
    student_name=input("Enter student name: ")
    student_id=input("Enter student Id: ")
    student_age=int(input("Enter student age: "))
    student_courses= input("Enter Courses (comma separated): ").split(",") ## Set to store unique courses

    student=(student_name, student_id, student_age, student_courses) ## Store as a tuple
    student_list.append(student) ## Add to list

    print(f"Student {student_name} added successfully\n")

def view_student (student_list):
    if not student_list:
        print("There is no student in the system")
        return
    
    for i in student_list:
        student_name, student_id, student_age, student_courses = i
        print(f"Student Name: {student_name}\n Student ID: {student_id}\n Student Age: {student_age}\n and the courses are: {','.join(student_courses)}\n")

def searceh (student_list):
    id=input("Enter the student id: ")
    for i in student_list:
        student_name, student_id, student_age, student_courses = i
        if id==student_id:
            print(f"Student Name: {student_name}\n Student ID: {student_id}\n Student Age: {student_age}\n and the courses are: {','.join(student_courses)}\n")
            print()
            return
    else:
            print("No student fount (*_*)")
            return

def remove (student_list):
    id=input("Enter the student id you want to remove: ")
    for i in student_list:
        student_name, student_id, student_age, student_courses = i
        if(student_id==id):
            student_list.remove(i)
            print(f"Student named {student_name} id {id} has removed")
            return
    else:
        print("Student not found")

def Courses (student_list):
    all_courses=set()
    for i in student_list:
        all_courses.update(i[3])
    print(f"Unique Courses offered {', '.join(all_courses)}\n")

def main():
    while(True):
        print("Student Data Management System")
        print("1. Add new student records (name, age, courses, student ID)")
        print("2. View all students.")
        print("3. Search for a student by ID")
        print("4. Remove a student")
        print("5. Display unique courses")
        print("6. Exit")
        choice = int(input("Eneter your choice: "))
        if choice==1:
            add_student (student_list)
        elif choice == 2:
            view_student (student_list)
        elif choice==3:
            searceh (student_list)
        elif choice == 4:
            remove (student_list)
        elif choice==5:
            Courses (student_list)
        elif choice==6:
            print("Exiting the program.")
            break
        else:
            print("Invalid choise, please try again!\n")

if __name__ == "__main__":
    main()