import crypt
import sys

def hash_salt_sha512(password, salt):
    salt_str = f"$6${salt}"  
    hashed_password = crypt.crypt(password, salt_str)
    return hashed_password

if len(sys.argv) < 3:
   print("Usage: python3 python.py <usersnames_file> <passwords_file>")
   sys.exit(1)

users_file = sys.argv[1]
passwords_file = sys.argv[2]


with open(users_file, 'r') as user_file:
    for line in user_file:
      user_info = line.split(':')  # Split by ':'
      salted_hashed_password = user_info[1]
      password_info = salted_hashed_password.split('$')  # Split by '$'

      username = user_info[0]
      salt = password_info[2]
      hashed_password = password_info[3]
      with open(passwords_file,'r') as pass_file:
        for password in pass_file:
          password = password.rstrip()
          guess_salt = hash_salt_sha512(password,salt)
          if(guess_salt==salted_hashed_password):
            print(f"Username: {username}")
            print(f"Clear-text Password: {password}")
            break;
        print(f"Password Scanning for: {username} finished.")
        print("-----------------------------------")

