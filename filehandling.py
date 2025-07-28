# Today's python Task-1 : Practice CRUD operations on file handling
file=open("./sample.txt" , 'r')
file.write("this is added from the python file")
file=open("./sample.txt" , 'r')
print(file.read())
file.writelines(["firstline \n" , "secondline \n" , "thirdline\n" ,"fourthline\n"])
file.close()
file.seek(3)
# print(file.read())
f=open('sample.txt','w')
f.flush()
print(f)
with open("sample.txt","r") as file:
    print(file.readline())
with open("sample.txt","w") as file:
     print(file.write("hiiii"))
with open("sample.txt","r") as file:
    print(file.readline())
Task-2 : Research topic on flush() and write()
write():
adds data to the file's buffer(temporary memory),not directly to the file
flush():
forces the buffer content to be written on the desk
Data written with write() may not be saved until flush() or close() is called.
flush() is useful in long-running programs to ensure data is saved immediately.
close() internally calls flush() before closing the file.

