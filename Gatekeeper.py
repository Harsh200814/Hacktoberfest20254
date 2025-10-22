# Your code here
username = input()
password = input()
if username=='admin' and password=='password123':
    print('Login successful')
elif username=='admin' or password=='password123':
    print('Check username or password')
else:
    print('Invalid credentials')
