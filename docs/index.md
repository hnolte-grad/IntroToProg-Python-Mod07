# 07_Pickling and Error Handling
### Hannah Clayton
### March 2, 2021
### Foundations of Programming: Python
### Assignment 07
### [Link to assignment docs](https://github.com/hnolte-grad/IntroToProg-Python-Mod07)

## I. Introduction
This document serves as a demonstration of my experience working through this week’s assignment module. In the ‘module objectives’ section, I highlight the intended goals for this week’s reading and instructional video as given by Professor Root, and in my own words communicate my understanding of the objectives. In the ‘assignment work-through’ section I show how I went about approaching the module’s assignment, and any issues or epiphanies I encountered in doing so. The overall intent of this document is to serve as both a reference for myself and others in the future and demonstrate my competency in the module to Professor Root.

## II. Module Objectives
### 1. Objectives
• What are the benefits of putting built-in Python command into functions?

• What are the benefits of using structured error handling?

• What are the differences between a text file and a binary file?

• How is the Exception class used?

• How do you "derive" a new class from the Exception class?

• When might you create a class derived from the Exception class?

• What is the Markdown language?

• How do you use Markdown on a GitHub webpage?

### 2. Objective Summary
This week’s module covered Python’s pickling method, error handling, and GitHub webpage designing and use. Using built-in Python commands in functions can be useful for simplifying program tasks and keep you from having to write out whole blocks of code for something as simple as printing a message or gathering user input. However, there are times where you will want your program to do something a certain way and can’t accomplish this using built-in functions. One such example of this is error handling.
Python’s standard error messages are not always clear, especially to a user not familiar with programming. To remedy this, we can change the message the user receives when an error has been encountered using a ‘try-except’ block. Try-except blocks capture an error using ‘try’, and then produce a response based on the ‘except’ section. Here is an example:
```
try:
    number = int('oops')
except ValueError:
    print('Error! You entered characters instead of a number, please try again.') 
```  
As you can see from the code above, I indicated that the ‘number’ variable should be an integer, but then input a string. This normally would result in a standard Python value error class message, but I modified that message using ‘except’ and the exception class. An ‘Exception’ is a Python object that is created every time an error is encountered, and it holds information about that error. The Exception object can be used to capture pretty much all error information, but as seen in my code above, you can use more specific exception classes to better modify your programs error handling. Another common exception class includes the EOFError, which can occur when you have reached the end of a file or there is no more input from an input function. To further modify your program’s exception handling you can ‘derive’ exception classes much like you would create other custom classes, using the original exception base class. 

![Image 2.1 Custom Exception class](https://github.com/hnolte-grad/IntroToProg-Python-Mod07/blob/main/docs/Screenshot%20(1333).png "tooltip text")

In Image 2.1 I do just this by defining a custom exception class (modValueError) and modifying the string message in the ‘try’ section of the block. Thus, when I input numerical values as the file name, I am given my custom message instead of Python’s class default. These custom exception classes can be useful when you would like to modify only a section of the error information (such as the string message) but leave other sections such as the exception class type.
  During this week’s module we were briefly introduced to working with binary type files. Binary files, unlike plain text files, are written in the computer’s binary language. This encrypts the data in the file, can reduce the file size, and enables the user to pull data from the same file using different programming languages. With Python you can use the ‘pickle’ function to both save and load data to and from a file in binary format using the ‘pickle.dump’ and ‘pickle.load’ methods and their associated arguments.
  Lastly, we touched on editing GitHub websites using Markdown, a programming language for website design. To use Markdown on a GitHub website, you must first create an index.txt document under the appropriate repository where you can input code to create your webpage. From there you can create and modify text in a variety of ways, such as creating headers of varying sizes using the pound symbol (#). Image 2.2 shows how I modified my GitHub webpage for this week’s assignment. 
  
![Image 2.2 GitHub webpage/MarkDown](https://github.com/hnolte-grad/IntroToProg-Python-Mod07/blob/main/docs/Screenshot%20(1335).png "tooltip text")

## II. Assignment Walkthrough
   This week’s assignment was straightforward, and what errors I did encounter were handled quickly. Alas, there was no ‘aha!’ moment this week, though I have come to realize that there are many times where simple is better. I wasted a good amount of time this week trying to make this program ‘cool’, resulting in my atypical nearly late submission. 
   
![Image 3.1 Pickle write error](https://github.com/hnolte-grad/IntroToProg-Python-Mod07/blob/main/docs/Screenshot%20(1336).png "tooltip text")

   I started writing this program by setting out my pseudo-code and writing and testing the two different goals of the program separately. I used a ‘main’ script to then copy and paste the different classes and functions once I was done testing them. You can see this, along with the one error I ran into while testing, in Image 3.1. The error arose from my function involved in saving data to a file in binary format using the ‘pickle.dump’ method. After a few minutes of google searching the error, I modified the function to be opened with a writing intent using the following block of code:
```
def pkl_write(file_name, list_of_rows):      # writes to file (gFileName, lstTable)
    with open(file_name, 'wb') as f:
        pkl.dump(list_of_rows, f)
    f.close()
```
   After all the classes and functions were created and functional, I wrote out the main body of my script, added comments, and was finished. One thing I was not able to do was get the binary document (‘PickleDoc.txt’ in my script) to populate before the program closing. The document always populated in PyCharm after the program completely ended. However, I know that the file was being created and modified because I was still able to load data back out from the file without completely ending the program.
