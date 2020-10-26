'''
File = open("test.txt", "a+" )
File.seek(0)
print(File.read())

File.close()
'''
"""
try:
    f = open("test1223.txt", "r")
except FileNotFoundError as result:
    print(result)

    f = open("test1223.txt",'w')
else:
    print("normal")

finally:
    print("must be run")
    f.close()
"""
with open("test122.txt" "r") as File
    print(File.read())

