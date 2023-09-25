import subprocess
import random
import sys

def create_user(username, password):
    subprocess.run(["useradd", username])
    proc = subprocess.Popen(['passwd', username], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate(input=f"{password}\n{password}\n".encode())

if len(sys.argv) != 2:
    print("Usage: file.py <passwords_file>")
    sys.exit(1)

password_file = sys.argv[1]

with open(password_file, 'r') as file:
    lines = file.readlines()

# Open a file to save the created usernames and their passwords
with open("chosen_passwords.txt", "w") as out_file:
    for i in range(30):
        username = "user" + str(i)
        password = random.choice(lines).strip()
        create_user(username, password)
        out_file.write(f"{password}\n")
