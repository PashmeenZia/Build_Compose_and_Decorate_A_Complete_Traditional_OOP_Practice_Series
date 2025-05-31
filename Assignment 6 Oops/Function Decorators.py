# Step 1: Decorator function
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper

# Step 2: Decorator apply karna
@log_function_call
def say_hello():
    print("Hello!")

# Step 3: Function call
say_hello()
