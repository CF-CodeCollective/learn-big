# Set up these variables to display your own name on your branch!
first_name = "Muneeb"
last_name = "Elyaman"

# This is done for a specific reason: any python script can be imported as a module, and all the code will
# be run from the top down. This lets you write setup code, but anything under this 'if' statement will only
# run if this file is launched directly, not imported.
if __name__ == "__main__":
    print("Hello, World!")
    print("Hello,", first_name, last_name)
