print('Create account now')

username = input('Enter your Username:')
password = input('Enter your password:')

print('Account created succesfully')
print('Login now!')

username2 = input('Enter your username:')
password2 = input('Enter your password:')

if username == username2 and password == password2:
  print('Login Successful')

else:
  print('Invalid Credentials')  