# FOR READING A FILE
# f = open('myFileRead.txt','r')
# text = f.read()
# print(text)
# f.close()

# # FOR WRITING A FILE 
# f = open('myFileWrite.txt','w')
# f.write('Hello World waheed')
# f.close()

# # FOR APPENDING A FILE
# f = open('myFileAppend.txt', 'a')
# f.write('  The text was appended')
# f.close()

# FOR READINGLINE OF A FILE
# f = open('myFileRead.txt', 'r')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)

# f = open('myFileReadLineMarks.txt', 'r')
# i = 0
# while True:
#     i = i+1
#     line = f.readline()
#     if not line:
#         break
#     s2 = int(line.split(",")[1])
#     s1 = int(line.split(",")[0])
#     s3 = int(line.split(",")[2])
#     print(f"Marks of student {i} in Maths is: {s1}")
#     print(f"Marks of student {i} in Enghlish is: {s2}")
#     print(f"Marks of student {i} in Computer is: {s3}")
#     print(line)

# SEEK() function allows you to move the current position within a file to a specific point in bytes.
# f = open('myFileWrite.txt', 'r')
# text = f.read()
# print(text)
# f.seek(5)
# TELL() returns the current position within the file, in bytes. This can be useful for keeping 
# track of your location within the file or for seeking to a specific position relative to the current position
# print(f.tell())



# truncate()  if you want to truncate the file to a specific size. OR want to 
# f= open('myFileTruncate.txt', 'a')
# f.write('hello waheed')
# f.truncate(7)
# with open('myFileTruncate.txt', 'r') as f:
#     print(f.read())

