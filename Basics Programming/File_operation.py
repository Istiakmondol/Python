#Normal file operation
def file_read (path):
    words= set()
    count=0
    with open(path,'r') as file:
        for i in file:
            i=i.lower().replace(" ", "")
            words.add(i)
        print(len(words))
        return words
    
        
path='G:\Data Analytics\Python-for-Data-Analytics\Basics Programming\Read me.txt'
x= file_read (path)
print(x)