
# this file allows to create hooks in various .py files
# the files in which the hooks are to be created are given as sys #arguments in running through terminal

import os
import sys

CHAR_COUNT_READ=0
CHAR_COUNT_WRITE=0

old_read = os.read
old_write = os.write
old_exit = sys.exit

def read_hook(fd, n):
    global CHAR_COUNT_READ
    ss = old_read (fd, n)
    CHAR_COUNT_READ += len(ss)
    return ss
def write_hook(fd, ss):
    global CHAR_COUNT_WRITE
    old_write (fd, ss)
    CHAR_COUNT_WRITE += len(ss)
def exit_hook(code):
    global CHAR_COUNT_READ
    global CHAR_COUNT_WRITE
    print("exit hook script termination")
    print("os.read() processed %d characters" % CHAR_COUNT_READ)
    print ("os.write() processed %d characters" % CHAR_COUNT_WRITE)
    old_exit(code)
def write_hook_install():
    global write_hook
    sys.write = write_hook
def exit_hook_install():
    global exit_hook
    sys.exit = exit_hook
def read_hook_install():
    global read_hook
    os.read = read_hook
def script_runner(filename):
    _globals=globals()
    _globals['__name__']='__main__'
    exec(filename, _globals)


if __name__ == '__main__':
    try:
        print('-------------')
        if len(sys.argv) > 1:
            print(sys.argv,'*************')
            read_hook_install()
            write_hook_install()
            exit_hook_install()
            script_name = sys.argv[1]
            sys.argv = sys.argv[1:]
            CHAR_COUNT_READ = 0
            CHAR_COUNT_WRITE = 0
            print ("running ", script_name)
            script_runner(script_name)
            print("normal script termination")
            print("os.read() processed %d characters" % CHAR_COUNT_READ)
            print("os.write() processed %d characters" % CHAR_COUNT_WRITE)
        else:
            print("Missing required argument of filename of Python script to run.")
            print("The Python script to run should make use of os.read or os.write.")
    except:
        print ("os-wrap exception handler")
        print ("os.read() processed %d characters" % CHAR_COUNT_READ)
        print ("os.write() processed %d characters" % CHAR_COUNT_WRITE)


