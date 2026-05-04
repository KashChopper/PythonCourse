"""
A function is a block of reusable code that is used to perform specific task. It helps in reducing code repetition and makes the code more organized and easier to read. Functions can take inputs, called parameters, and can return outputs. They are defined using the `def` keyword in Python.

SYNTAX:

def function_name(parameters):
    # function body
    return output
"""

# Example of a simple function that takes two numbers as input and returns their sum

def sum(a,b):
    return(a+b)


print(sum(10,40))

"""
TYPES OF FUNCTION
1. Built-in Functions: These are functions that are already defined in Python and can be used directly. Examples include `print()`, `len()`, `type()`, etc.
2. User-defined Functions: These are functions that are defined by the user to perform specific tasks. They can be created using the `def` keyword.

TYPES OF USER-DEFINED FUNCTIONS
1. Functions without parameters and without return value: These functions do not take any input and do not return any output. They perform a specific task and may print the result or modify a global variable.
2. Functions with parameters and without return value: These functions take input parameters but do not return any output. They perform a specific task using the input parameters and may print the result or modify a global variable.
3. Functions without parameters and with return value: These functions do not take any input but return an output. They perform a specific task and return the result to the caller.
4. Functions with parameters and with return value: These functions take input parameters and return an output. They perform a specific task using the input parameters and return the result to the caller.
5. ADVANCED PARAMETERS
   a. Default Parameters: These are parameters that have a default value. If the caller does not provide a value for the parameter, the default value will be used.
   b. Variable-length Parameters: These are parameters that can take a variable number of arguments. They are defined using `*args` for non-keyword arguments and `**kwargs` for keyword arguments.
   
"""