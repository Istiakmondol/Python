## Basic Data Types
'''
Integer
string
float
boolean
'''

## Advance Data Types
'''
List/Array ex. lst=["name", 1, 2, 3.4,True] (it can contain all kind of data types inside it. it behaves like array)
Tuples ex. lst=("name", 1, 2, 3.4,True) (Almost same as List)
Sets
Dictionaries
'''

'''
## Booleans
a=10
b=12
print(a==b)
print(type(a==b))
'''
'''
## List
lst=["Md.", "Istiak", "Mondol","DOB->",13,2,2001,"Height->",5.7,"Student->",True]
print(lst[1])
print(lst)
print(lst[1:])
print(lst[0:3])
print(lst[-1])

## Modifying the list elements

lst[2]="Nayem"
print(lst)
fruits=["Apple", "Banana", "Cherry", "Kiwi"]
print(fruits)

fruits.append("Orange") ## it will add orange at the end of the list
print(fruits)

fruits.insert(1,"Banana") ## it will insert item at the mentioned position in the list
print(fruits)
fruits.insert(1,"Watermalon") ## it will insert item at the mentioned position in the list
print(fruits)

fruits.remove("Banana") ## it will remove that particular string from the list
print(fruits)

popped_fruits=fruits.pop() ## it will remove and return the last element from the list
print(popped_fruits)
print(fruits)

print(fruits.count("Banana")) ## it will count the exact number of that item

fruits.sort() ## it will sort the items of a list alphabatical order
print(fruits)

fruits.reverse() ## it will reverse the list
print(fruits)

fruits.clear() ## it will empty the list
print(fruits)


##Slicing list
num=[1,2,3,4,5,6,7,8,9]
print(num[2:5])
print(num[:5])
print(num[5:])
print(num[::2])
print(num[::-2])

##iterating over list
name=["md","istiak","mondol","nayem","nahid","ragib"]
name.sort()
print(name)
##
for i in name:
    print(i)

##
for index,i in enumerate(name): ##iterate with index also
    print(index,i)

##
lst=["md","istiak","mondol","nayem","nahid","ragib"]
length=[]
for i in lst:
    length.append(len(i))
print(length)

##
lst2=[]
for i in range(1,11):
    if i%2==0 :
        lst2.append(i)
print(lst2)
'''

## Tuples
numbers=(1,1,2,3,4,5,6,7,8)
print(type(numbers))
mixed_tuple=("Md", "Istiak", "mondol", 5, 6, 7, False)
print(type(mixed_tuple))
concate_tuple= numbers + mixed_tuple
print(type(concate_tuple))
print(concate_tuple)

## Emmutable Nature of Tuples
## it means one a element assigned, it can't be changed
## the procedure of changing an element from tuple is (tuple-> list[make changes with element]-> Tuple) 
## numbers[1]="name" -> this will give you error (here number is a tuple)
print(type(numbers))
print(numbers)
lst_cnv=list(numbers)
print(type(lst_cnv))
lst_cnv.insert(1,"Istiak")
numbers=tuple(lst_cnv)
print(type(numbers))
print(numbers)


## Touple Method
print(numbers.count(1)) ## it will count the appearance of that item in the touple

print(numbers.index(3)) ## it will show the item at the mentioned index

### packing & unpacking Touple
packed_tuple=1,"Hello",3.14
print(packed_tuple)

# unpacking Touple
a,b,c=packed_tuple
print(a)
print(b)
print(c)

# unpacking Touple using star
num=(1,2,3,4,5,6)
first,*middle,last=num
print(first)
print(middle)
print(last)

## Nasted tuples
#list
lst=[[1,2,3,4],[1,"hello","c"],[1.5,"hdcb",4,True]]
print(lst[0][3])
print(lst[2][:2:1])
# Nasted tuples
nested_tuples=((1,2,3),("a","b","c"),(True,False))
print(nested_tuples[0][::-1])
print(nested_tuples[1][::-1])

##iterating over tuples through loop
for i in nested_tuples:
    for j in i:
        print(j,end=" ")
    print()