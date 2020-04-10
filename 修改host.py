class addhost():


    pingaddress='google.com'

    def openhost(self):
        import sys, os
        import re, requests
        if os.name=='nt':
            host= open(r'C:\Windows\System32\drivers\etc\hosts', 'r+')

            # hostOld=f.read()
            # hostNew= ""
            # hostNew='\r\n=========================\r\n'+hostNew
            # f.write(hostNew)
            # f.close()
        if os.name=='posix':
            hosts= open('/etc/hosts','a')
        if os.name=='mac':
            hosts= open('Private/etc/hosts', 'a')
        else:
            exit(0)

    def pingip(self):
        pingaddress='google.com'
        import socket
        try:
            pingip=socket.gethostbyname(str(pingaddress))
            ip= pingip+'......'
        except  socket.gaierror:
            print('dns 解析失败')

if __name__ == '__main__':
    oss=addhost()
    oss.openhost()


