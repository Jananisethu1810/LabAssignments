#Open a file

fi=open("file1.txt", "r+");
print ("Name of the file : ", fi.name);
print ("Access Mode of the file : ", fi.mode);
#fi.write("Python is a high level programming language!!!");
#fi.write("\nPython is easy to learn...");
str=fi.read(50)
print(str);

# Check current position
position = fi.tell()
print ("Current file position : ", position);

position = fi.seek(0, 0);
str = fi.read(10)
print ("Again read String is : ", str)


fi.close();


