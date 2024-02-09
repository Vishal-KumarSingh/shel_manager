import os
import json

import scripts
command_file = "command.json"
session_file = "session.json"
user = {}
command = {}
cwd = ""
def create_session():
    print("Welcome User looks like it is your first installation")
    name = input("Kindly input your name -> ")
    print("Hello " , name , " ")
    user["name"] = name
    userfile = open('session.json' , 'w')
    json.dump(user , userfile)
def validate_installation():
    if not os.path.exists('command.json'):
        print("Command json not found !! Creating one..")
        open('command.json' , 'w')
    if not os.path.exists('session.json'):
        print("Session json not found !! Creating one..")
        create_session()
    if not os.path.isdir('shell_cmd'):
        print("Shell folder not found !! Creating the folder..")
        os.mkdir('shell_cmd')

print("Welcome to Shell Manager. You can declare scripts commands and run as per their needs !!")
print("Enjoy the software")
#Validating evertyhing is working fine or not .
validate_installation()
#Validation is done now initializing the objects
command = open(command_file , "r").read()
user = open(session_file , "r").read()


while True:
    command = input(cwd + "->>>")
    if(command == "create shell_cmd"):
        scripts.create_shell_cmd()
        continue
    if(command[:4] == "exec"):
        scripts.executeShellCMD(command)
        continue
    if(command== "x"):
        break
    scripts.run_command(command)


print("Exiting the Shell Manager !! ")
json.dump(user , open(session_file,'w'))
json.dump(command , open(command_file , 'w'))
