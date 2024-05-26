import getpass

"""
logout funcionality

author: Muhammed Adnan on May 10th, 2024
purpose: login user
paramaeters: username, password
return: status
updated by: - sreethu on May 15th, 2024 - Add forget password funcinality
"""

username = input("Enter Username: ")
password = getpass.getpass("Enter your password: ")

def forgetPasswrod(email: str) -> bool:
  return True if email.exist() else False

print(f"username: {username}, password: {password}")
