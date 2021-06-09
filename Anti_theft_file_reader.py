import os, getpass#getpass is pre installed and I think os is too, but check
file = input('file>>> ')
password = 'Password'#you can change this to whatever you want
username = 'zacharysummers'#in the shell type import getpass, press enter, now type getpass.getuser(),press enter, use the output as username
access = False
if getpass.getuser() == username:
    guess = input('Password»»» ')
    if guess == (password):
        access = True
else:
    access = False
if access == False:
    os.remove(file)
    os.remove("/Users/zacharysummers/Desktop/Code/Anti_theft_file_reader.py")#replace the string with the directory of this python file
elif access == True:
    f = open(file, "r")
    print(f.read())
    f.close()
    print(file)