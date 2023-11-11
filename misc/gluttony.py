import socket

hostname = "mctf-game.ru"
port = 4040
newstring = ""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, port))
#s.sendall(content)
#s.shutdown(socket.SHUT_WR)
while True:
    data = s.recv(4096)
    if len(data) == 0:
        print("break")
    newstring += data.decode("utf-8")
    print("hui: ", data.decode("utf-8"))
    if newstring.find(":") != -1:
        newstring = newstring.split("GO!")[-1]
        newstring = newstring.split("\n")[4:-2]
        newstring = list(map(lambda x: int((x.split('|')[1]+x.split('|')[-2]).replace(' ','').split('.')[-1]), newstring))
        newstring = newstring.index(max(newstring)) + 1
        newstring = str(newstring)
        print(newstring)
        s.sendall(bytes(newstring, "utf-8"))
        newstring = ""
print("Connection closed.")
s.close()