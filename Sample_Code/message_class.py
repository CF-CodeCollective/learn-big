# Step 1: Decide what you want your class to do
# In this case, hold message content and likes (a string and an integer)

# Step 2: Declare a class
class SampleClass:
    """A simple example class (this line shows up when you hover over an instance of this class)"""
    # Declares a variable stored in this class; no different from any other variable
    variable = 0

    # Starting data can be assigned with a 'constructor', which is a function that runs
    # when you make an instance of a class.
    # In Python, the function is __init__(self, ...)
    # You can restrict allowed input types by following the parameter name with a colon and the type code
    def __init__(self, variable: int):
        # Within a class, use self.x to access a variable or function 'x'
        self.variable = variable


# Step 3: Instantiate the class (defining a custom constructor allows you to pass in variables)
test_class = SampleClass(10)

# Step 4: Test the class
print(test_class.variable)
