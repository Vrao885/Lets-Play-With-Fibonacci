# Initialize variables for the first two numbers in the sequence
a, b = 0, 1

# Print the Fibonacci series between 0 and 50
print("Fibonacci Series between 0 and 50:")
print(a)

while b <= 50:
    print(b)
    a, b = b, a + b