# File handling in python
# A file is a named location on disk to store related information. It is used to permanently store data in a non-volatile memory (e.g. hard disk).
# Since, random access memory (RAM) is volatile which loses its data when computer is turned off, we use files for future use of the data.
# When we want to read from or write to a file we need to open it first. When we are done, it needs to be closed, so that resources that are tied with the file are freed.
# Hence, in Python, a file operation takes place in the following order:
# 1. Open a file
# 2. Read or write (perform operation)
# 3. Close the file
# Common reall world examples where file handling is used:
# 1. Storing data in a file
# 2. Reading data from a file
# 3. Writing data to a file
# 4. Appending data to a file
# 5. Creating a new file
# 6. Deleting a file
# 7. Renaming a file
# 8. Checking if a file exists
# 9. Checking if a file is readable
# 10. Checking if a file is writable
# 11. Checking if a file is executable
# 12. Checking if a file is a directory
# 13. Checking if a file is a file
# 14. Checking if a file is empty
# 15. Checking if a file is hidden
# 16. Checking if a file is a symlink
# 17. Checking if a file is a block device
# 18. Checking if a file is a character device
# 19. Checking if a file is a socket
# 20. Checking if a file is a FIFO
# 21. Checking if a file is a regular file
# 22. Checking if a file is a symbolic link
# 23. Checking if a file is a mount point
#
# Common file operations:

# Example 1: Creating a file
f = open("demofile.txt", "w")
f.write("This is a new file")
f.close()
# Output: This is a new file

# Example 2: Reading a file
f = open("demofile.txt", "r")
print(f.read())
f.close()

# Example 3: Writing to a file
f = open("demofile.txt", "w")
f.write("This is a new file")
f.close()
f = open("demofile.txt", "r")
print(f.read())
f.close()
# Output: This is a new file

# Example 4: Appending to a file
f = open("demofile.txt", "a")
f.write("This is a new file")
f.close()
f = open("demofile.txt", "r")
print(f.read())
f.close()

# Example 5: Deleting a file
import os
os.remove("demofile.txt")
# Output: FileNotFoundError: [Errno 2] No such file or directory: 'demofile.txt'

# Example 6: Renaming a file
import os
os.rename("demofile.txt", "mydemofile.txt")
# Output: mydemofile.txt

# Example 7: Checking if a file exists
import os
if os.path.exists("mydemofile.txt"):
    print("The file exists")
else:
    print("The file does not exist")
# Output: The file exists
    
# Example 8: Checking if a file is readable
import os
if os.access("mydemofile.txt", os.R_OK):
    print("The file is readable")
else:
    print("The file is not readable")
# Output: The file is readable
    
# Example 9: Checking if a file is writable
import os
if os.access("mydemofile.txt", os.W_OK):
    print("The file is writable")
else:
    print("The file is not writable")
# Output: The file is writable
    
# Example 10: Checking if a file is executable
import os
if os.access("mydemofile.txt", os.X_OK):
    print("The file is executable")
else:
    print("The file is not executable")
# Output: The file is not executable
    
# Example 11: Checking if a file is a directory
import os
if os.path.isdir("mydemofile.txt"):
    print("The file is a directory")
else:
    print("The file is not a directory")
# Output: The file is not a directory

# Example 12: Checking if a file is a file
import os
if os.path.isfile("mydemofile.txt"):
    print("The file is a file")
else:
    print("The file is not a file")
# Output: The file is a file
    
# Example 13: Checking if a file is empty
import os
if os.path.getsize("mydemofile.txt") == 0:
    print("The file is empty")
else:
    print("The file is not empty")
# Output: The file is not empty
    
# Example 14: Checking if a file is hidden
import os
if os.path.isfile("mydemofile.txt"):
    if os.path.basename("mydemofile.txt").startswith("."):
        print("The file is hidden")
    else:
        print("The file is not hidden")
# Output: The file is not hidden

# Example 15: Checking if a file is a symlink
import os
if os.path.islink("mydemofile.txt"):
    print("The file is a symlink")

# Example 16: Checking if a file is a block device
import os
if os.path.isblock("mydemofile.txt"):
    print("The file is a block device")
else:
    print("The file is not a block device")

# Example 17: Checking if a file is a character device
import os
if os.path.ischar("mydemofile.txt"):
    print("The file is a character device")
else:
    print("The file is not a character device")

# Example 18: Checking if a file is a socket
import os
if os.path.issocket("mydemofile.txt"):
    print("The file is a socket")
else:
    print("The file is not a socket")

# Example 19: Checking if a file is a FIFO
import os
if os.path.isfifo("mydemofile.txt"):
    print("The file is a FIFO")
else:
    print("The file is not a FIFO")

# Example 20: Read a file line by line
f = open("mydemofile.txt", "r")
for x in f:
    print(x)
f.close()

# Example 21: Read a file line by line using readline()
f = open("mydemofile.txt", "r")
print(f.readline())
f.close()

# Example 22: Read a file line by line using readlines()
f = open("mydemofile.txt", "r")
print(f.readlines())
f.close()

# Print all methods and properties of the file object:
f = open("mydemofile.txt", "r")
print(dir(f))
