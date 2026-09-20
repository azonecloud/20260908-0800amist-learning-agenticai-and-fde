# File operations in Python allow you to interact with files on your computer's file system. 
# Python provides several built-in functions and methods to perform various file operations, such as reading from and writing to files. 

# Here's an overview of the most commonly used file operations in Python:


# 1. **Writing to a File:**
    # To write content to a file, use the `write()` method in write mode. 
    # Note that using `'w'` mode will overwrite the existing content of the file.

file = open('myfile.txt', 'w')

file.write("Hello, this is a sample text.\n")
file.write("Writing to a file is easy!\n")

file.close()


# 2. **Reading from a File:**
file = open('myfile.txt', 'r')

print(file.read())
file.close()


# 3. **Appending to a File:**
# To append content to an existing file, open the file in append mode `'a'`.
# Appending to a file
file = open('myfile.txt', 'a')
file.write("This text is appended.\n")

file = open('myfile.txt', 'r')
print(file.read())

file.close()

# 4. **Using 'with' Statement (Recommended):**
# A better practice to work with files is to use the `with` statement, which automatically handles file closing, even if an exception occurs during file operations.

# Using 'with' statement to automatically close the file
with open('myfile.txt', 'r') as file:
    content = file.read()
    # Perform file operations as needed
# File is automatically closed after the 'with' block
print(content)


# 5. **Closing a File:**
# It's essential to close the file after performing file operations to release the resources associated with it.
# Closing the file
file.close()


# Always remember to close the file after you are done with it, especially when using the standard `open()` method. 
# Alternatively, you can use the `with` statement to ensure proper handling of file resources and to avoid potential issues with unclosed files.
# Keep in mind that file operations are subject to permissions and restrictions imposed by the operating system. 
# Ensure that you have the necessary permissions to read from and write to the files you are working with.'''