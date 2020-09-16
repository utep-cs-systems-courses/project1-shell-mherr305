#! /usr/bin/env python 3
#Manuel Herrera
#Unix Shell project

import os, sys, time, re

#Prints a prompt and evaluate the input
#Check for PSI
def main():
    while True:
       if 'PS1' in os.environ:
           os.write(1, (os.environ['PS1']).encode())
       else:
           os.write(1 , ("$ ").encode())
       inputLine = "$ "
       inputLine = input()
    

       if inputLine.split() == "exit":
           os.write(1, ("Program terminated\n".encode())
           sys.exit(0)
       if 'cd' in inputLine:                               #Validates changes directory
           chan_dir = inputLine.split("cd")[1].strip()
           try:
               os.chdir(chan_dir)
           except FileNotFound:
               os.write(1, ("No directory found\n").encode())
           continue
                 
# pid = os.getpid()
os.write(1, ("About to fork (pid:%d)\n" % pid).encode())
rc = os.fork()

#if-else statement for rc fail,execute,wait                 
if rc < 0:
    os.write(2, ("Fork failed, returning %d\n" % rc).encode())
    sys.exit(1)
                 
#rc elif for child
#Initialized the pipe acording to user input
elif rc==0:
    if "|" in inputLine:
        line = inputLine.split("|")
        line_command = pipe[0].split()
        pipe_read = os.pipe()                   #pipe function for read
        pipe _write = os.pipe()                 #pipe function for write
        for fi in (pipe_read, pipe_write):
            os.set_inheritable(fi, True)

        pipe_fork = os.fork()
        if pipe_fork < 0:
            os.write(2 , ("Fork failed, returning\n").encode())
            sys.exit(1)

        if pipe_fork ==0:
            os.close(1)
            os.dup(pipe_write)                #use os.dup function for write pipe
            os.set_inheritable(1, True)       #Set inheritable to 1
            for fid in (pipe_read, pipe_write)
                 os.close(fid)
            exe(line[0].strip())
        else:
            os.close(0)
            os.dup(pipe_read)                 #use os.dup function for read pipe
            os.set_inheritable(0, True)       #Set inheritable to 0
            for fid in (pipe_read, pipe_write):
                 os.close(fid)
            exe(line[1].strip())
#def exe check the line input and evaluate the symbols "<" ">" for redirection
def exe(line):                  
    pid = os.getpid()
    rc= os.fork()

    if rc < 0:
        sys.exit(1)
    elif rc == 0:
        if ">" in line or "<" in line:
            if ">" in line:
                line.remove(">")
                os.close(1)
                os.open(line[-1], os.O_CREAT | os.O_WRONLY);
                os.set_inheritable(1, True)
            else:
                os.close(0)
                sys.stdin = open(line[-1], "r")
                os.set_inheritable(0, True)
                    
         
                 
    os.write(1, ("Child: My pid==%d.  Parent's pid==%d\n" % (os.getpid(), pid)).encode())
    args = ["wc", "p3-exec.py"]
    for dir in re.split(":", os.environ['PATH']): #try each directory in the path
    program = "%s/%s" % (dir, args[0])
    os.write(1, ("Child: ...trying to exec %s\n" % program).encode())
    try:
        os.execve(program, args, os.environ) #try to exec program
    except FileNotFoundError:                #...expected
        pass                                 #...fail quietly

    os.write(2, ("Child: Could not exec %s\n" % args[0]).encode())
    sys.exit(1)                              #terminate with error

    else:                                        #parent (forked ok)
        os.write(1, ("Parent: My pid=%d. Child's pid=%d\n" % (pid, rc)).encode())
        childPidCode = os.wait()
        os.write(1, ("Parent: Child %d terminated with exit code %d\n" % childPidCode). encode())                    
if __name__=="__main__":
    main()
