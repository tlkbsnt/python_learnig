def my_function():
    global x
    x = "Global variable using global keywork"
my_function()

print(x)  # accessing the outside the function value of x