library=[]
def add_book():
    try:
        book={}
        title=input("Enter Book Name: ")
        book["title"]=title.title()
        print()
        author=input("Enter Author Name: ")
        book["author"]=author
        print()
        genre=input("Enter Book Genre: ")
        book["genre"]=genre
        print()
        year=int(input("Enter the Publication year: "))
        book["year"]=year
        print()
        rating=float(input("Enter Book Rating: "))
        book["rating"]=rating
        print()
        library.append(book)
    except Exception as main:
        print(main)

def View_all_books():
    try:
        for book in library:
            print(book.items())
    except Exception as main:
        print(main)

def Search():
    try:
        src=input("Enter the title of the book you are looking: ").title()
        for book in library:
            if src in book["title"]:
                print("Book Found")
                for key,value in book.items():
                    print(f"{key}: {value}\n")
                break
    except Exception as main:
        print(main)

def update():
    try:
        src=input("Enter the title of the book you are looking: ").title()
        for book in library:
            if src in book["title"]:
                print("Book Found")
                while(True):
                    choice=int(input("Which field do you want to update: 1)Title 2)Author 3)Genre 4)Year 5)Rating 6)EXIT\n"))
                    if choice==1:               
                        book["title"]=input("Enter Book Name: ").title()
                    elif choice==2:
                        book["author"]=input("Enter Author Name: ")
                    elif choice==3:
                        book["genre"]=input("Enter Book Genre: ")
                    elif choice==4:
                        book["year"]=int(input("Enter the Publication year: "))
                    elif choice==5:
                        book["rating"]=float(input("Enter Book Rating: "))
                    elif choice==6:
                        break
                print("Sccessfully Updated")
    except Exception as main:
        print(main)

def delete():
    try:
        src=input("Enter the book title you want to delete: ")
        for book in library:
            if src in book["title"]:
                library.remove(book)
        print("Sccessfully Deleted") 
    except Exception as main:
        print(main)         

def Save():
    try:
        with open("Library.txt", mode='w') as file:
            for book in library:
                content=str(book)
                file.write(content+'\n')
            print("Saved successfully to Library.txt!")
            library.clear()
    except Exception as main:
        print(main)

def load():
    try:
        with open("Library.txt", mode='r') as file:
            content=file.readlines()
            for lines in content:
                book=eval(lines.strip())
                library.append(book)
            print(" Library loaded successfully!")
    except Exception as main:
        print(main)

def main():
    print("Personal Library Management")
    while(True):
        print("Choose an option between (1-8)\n")
        print("1. Add a Book \n")
        print("2. View All Books\n")
        print("3. Search for a Book\n")
        print("4. Update a Book\n")
        print("5. Delete a Book\n")
        print("6. Save\n")
        print("7. Load\n")
        print("8. EXIT")
        print()
        choice = int(input())
        if choice==1:
            add_book()
        elif choice==2:
            View_all_books()
        elif choice==3:
            Search()
        elif choice==4:
            update()
        elif choice==5:
            delete()
        elif choice==6:
            Save()
        elif choice==7:
            load()
        elif choice==8:
            break
        else:
            print("Invalid choice.\n") 

if __name__=="__main__":
    main()