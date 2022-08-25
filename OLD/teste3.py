import os
ip = "8.8.8.8"
port = "53"
''' send to /dev/null 2>&1 to suppress terminal output '''
res = os.system("nc -w 1 -vnzu "+ip+" "+port+" > /dev/null 2>&1")
if res == 0:
    print("port alive")
else:
    print("port dead")
