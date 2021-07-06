# https://stackoverflow.com/questions/53255636/how-to-open-a-text-file-from-my-desktop-while-using-python-3-7-1-in-terminal

# myfile = open("/Users/David/Desktop/test.txt","r") #returns file handle
# myfile.read() # reading from the file
# myfile.close() # closing the file handle, to release the resources.

with open(r"/Users/jsidd/PycharmProjects/javed-raoon/corefinta_scratchpad/email_practice/test.txt", "r") as file1:
    FileContent = file1.read()
    print(FileContent)
