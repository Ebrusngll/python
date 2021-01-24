with open("C:/Users/Ebru/Downloads/example1.txt","r") as file1:
    file_stuff=file1.read()
    print(file_stuff)
print("file is closed mode ",file1.closed)
print(file_stuff)
lines = ["meliha\nebru\nşengül"]
with open("C:/Users/Ebru/Downloads/example2.txt","w") as file:
    for line in lines:
        file.write(line)



