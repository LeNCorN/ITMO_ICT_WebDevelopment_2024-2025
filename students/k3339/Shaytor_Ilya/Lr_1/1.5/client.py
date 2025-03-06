import socket

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.connect(("127.0.0.1", 5000))

discipline = input()
grade = input()
body =  f"discipline={discipline}&grade={grade}"
POST = f"POST http://localhost:5000 HTTP/1.1\r\nContent-Length: {len(body)}\r\n\r\n{body}"
print(POST)

serv.sendall(POST.encode())