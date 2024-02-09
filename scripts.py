import os
import subprocess
def create_shell_cmd():
    print("Enter the shell command file name")
    scriptName = input("-->")
    if os.path.exists("shell_cmd/"+scriptName):
        print("File already exists You can update the file ")

    else:
        scriptFile = open("shell_cmd/"+scriptName , 'w')
        print("Created new shell command file")
        command_arr = []
        i=1
        while True:
            cmd = input("["+str(i)+"]->")
            if cmd=="x":
                break;
            command_arr.append(cmd)
            i=i+1
        commands = "\n".join(command_arr)
        print("Wrote the script file successfully")
        scriptFile.write(commands)

def run_command(command):
    process = subprocess.Popen(command , shell=True)
    process.wait()

def executeShellCMD(command):
    fileName = command[4:].strip()
    if os.path.exists("shell_cmd/"+fileName):
        commands = open("shell_cmd/"+fileName).read().split('\n')
        #print(commands)
        for command in commands:
            print("Executing --> " + command)
            run_command(command)

    else:
        print("Shell command file does't exist.. Try creating using create shell_cmd command !!")