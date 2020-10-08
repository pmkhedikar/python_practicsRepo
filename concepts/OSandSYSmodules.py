import  os
import sys

#os operating system depending functionalities
#access to interpreter functions



print(os.name)
print(os.getcwd())
print(os.error)
#print(os.rename())
#Executing a shell command
#os.system()



# #Returns the current working directory.
print(os.getcwd())
# Return the current process’s user id.
#print(os.getuid())
#
# Returns the real process ID of the current process.
# os.getpid()
#
# Set the current numeric umask and return the previous umask.
# os.umask(mask)
#
# Return information identifying the current operating system.
# os.uname()
#
# Change the root directory of the current process to path.
# os.chroot(path)

#print("Hello {}. Welcome to {} tutorial".format(sys.argv[1], sys.argv[2]))
print(type(sys.path)) # current working directory ,dir listed in python env path