import os
import subprocess
import sys


if sys.platform in ("linux", "linux2", "darwin"):
    cmd = "ifconfig"
    os.system(cmd)
    subprocess.call(cmd, shell=True)
    myprocess = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    output, err = myprocess.communicate()
    print("output==============\n", output)
    print("err=================\n", err)
elif sys.platform == "win32":
    # print(os.system('dir /x C:\Python27'))
    # print(call('dir /x C:\Python27', shell=True))

    myprocess = subprocess.Popen(r"diras /x C:\Python27", shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output, err = myprocess.communicate()
    print("output==============\n", output.decode("utf-8"))
    print("err=================\n", err.decode("utf-8"))
else:
    print("unhandled platform :", sys.platform)
    exit(1)