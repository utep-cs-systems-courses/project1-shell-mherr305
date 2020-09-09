#! /usr/bin/env python 3
#Manuel Herrera
#Unix Shell project

import os, sys, time, re

while True:
    inputLine = input("$ ")
    if inputLine.split() == "close":
        os.write(1, ("Program terminated\n".encode())
        sys.exit(0)
                 
pid = os.getpid()
os.write(1, ("About to fork (pid:%d)\n" % pid).encode())
rc = os.fork()

if rc < 0:
    os.write(2, ("Fork failed, returning %d\n" % rc).encode())
    sys.exit(1)
                 
elif rc==0:
    os.write(1, ("Child: My pid==%d.  Parent's pid==%d\n" % (os.getpid(), pid)).encode())
    args = ["wc", "p3-exec.py"]
    for dir in re.split(":", os.environ['PATH']):
    program = "%s/%s" % (dir, args[0])
    os.write(1, ("Child: ...trying to exec %s\n" % program).encode())
    try:
        os.execve(program, args, os.environ)
    except FileNotFoundError:
        pass

    os.write(2, ("Child: Could not exec %s\n" % args[0]).encode())
    sys.exit(1)

else:
    os.write(1, ("Parent: My pid=%d. Child's pid=%d\n" % (pid, rc)).encode())
    childPidCode = os.wait()
    os.write(1, ("Parent: Child %d terminated with exit code %d\n" % childPidCode). encode())                    
