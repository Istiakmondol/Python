## Basic Data Types
'''
Integer
string
float
boolean
'''

## Advance Data Types

#List/Array ex. lst=["name", 1, 2, 3.4,True] (it can contain all kind of data types inside it. it behaves like array)
#Tuples ex. tuple=("name", 1, 2, 3.4,True) (Almost same as List)
#Sets ex. set={}"name", 1, 2, 3.4,True} (Set of unique items)
#Dictionaries



## Booleans
a=10
b=12
print(a==b)
print(type(a==b))


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
    

## Set

#create a set
my_set={1,2,3,4,5,6,7,"istiak"}
print(type(my_set))
print(my_set)

#create empty set
my_empty_set=set()
print(type(my_empty_set))
print(my_empty_set)

##basic operation of set
empty_set=set([1,2,3,4,5])
print(empty_set)

#1 duplicate element of set
empty_set=set([1,2,3,4,5,3,2,4])
print(empty_set)

#1 Adding element
my_set.add(7)
print(my_set)

#Removing elements
my_set.remove("istiak")
print(my_set)

#won't give error if the element is not present there
my_set.discard(10)
print(my_set)

#Removing elements using pop method
removed_element=my_set.pop()
print(removed_element)
print(my_set)

#clear all the elements
my_set.clear()
print(my_set)

### set membership test
my_set={1,2,3,4,5}
print(3 in my_set)
print(5 in my_set)

### Mathematical operation
my_set={1,2,3,4,5,6}
my_set2={3,4,5,6,7,8,9}

#Union
union_set=my_set.union(my_set2)
print(union_set)

#Intersection
intersection_set=my_set.intersection(my_set2)
print(intersection_set)

#Intersection_Update
intersection_update_set= my_set.intersection_update(my_set2)
print(my_set)

my_set={1,2,3,4,5}
my_set2={3,4,5,6,7}

#Difference
Diffrence_set= my_set.difference(my_set2)
print(Diffrence_set)

#Difference_update
Diffrence_set= my_set.difference_update(my_set2)
print(my_set)

my_set={1,2,3,4,5}
my_set2={3,4,5,6,7}

# Symmetric Difference
Sym_Diffrence_set= my_set.symmetric_difference(my_set2)
print(Sym_Diffrence_set)

#Set Method
my_set={1,2,3,4,5,6,7}
my_set2={3,4,5,6,7}

#is subset?
subset_set=my_set2.issubset(my_set)
if subset_set==True:
    print("Yes")
else:
    print("No")

#is superset?
super_set=my_set.issuperset(my_set2)
if super_set==True:
    print("Yes Super set")
else:
    print("Not super set")

##counting unique words is text
text="we are learning set operation"
word=text.split()
print(type(word)) ## it is not in 'List' order

unique_words=set(word) ##now it has converted to 'Set'
print(unique_words)
print(len(unique_words))

