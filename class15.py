# import os,stat,platform   #buil in library
# import sys

#x = sys.maxsize()
#print(x)

# fd = os.open( "test.txt", os.O_WRONLY)
# os.chmod(fd,os.O_RDONLY)
#os.chmod


# xyz = os.listdir("d:/kali")
# print(xyz)

#rs = os.makedirs("d:/deepak/xyz/dd")

# xyz = os.listdir("d:/deepak")
# print(xyz)



# from dotenv import load_dotenv
# load_dotenv()
# print(platform.system())
# print(os.getenv("HOME"))
# print(os.getlogin())
# print(os.getpid())
# pId=os.getpid()
# if(platform.system() == "UNIX"):



#Change file mode to Write by owner
#os.chmod("test.txt", stat.S_IWRITE)

#os.setpriority(os.PRIO_PROCESS, pId, 5)


# fd = os.open( "test.txt", os.O_WRONLY)
# os.chmod(fd,os.O_RDONLY)


import os,stat,platform   #buil in library
fd = os.chmod( "test.txt", stat.S_IWRITE)

f = open("test.txt",'w')
f.write("kumar")

f.write("jjjj")


# print(f.read(20))

