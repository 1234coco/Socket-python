A = 0
import socket
import time
try:
    PVU = open("TVP.csv",mode="r",encoding="utf-8-sig")
    PU = PVU.readline()
    UP = PU.split(",")
    SADN = 2
    SA = 0
    SA = int(SA)
    SADN = int(SADN)
    D = 1
    C = "Ghép thành công"
    KC = "Ghép không thành công.\nVui lòng thử lại"
    Host = "127.168.1.209"
    Port = 60432
    Format = "utf32"
    PVU = open("TVP.csv",mode="r",encoding="utf-8-sig")
    PU = PVU.readline()
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    HL = "Đăng nhập hợp lệ"
    KHL = "Đăng nhập không hợp lệ"
    s.bind((Host, Port))
    s.listen()
    print("server side")
    print("server:", Host, Port)
    print("chờ")
    conn, addr = s.accept()
    print("clint address:", addr)
    print("conn:",conn.getsockname())
    user = conn.recv(50).decode(Format)
    password = conn.recv(100).decode(Format)
    if UP[0] == user and UP[1]== password:
        print(user)
        print(password)
        conn.sendall(HL.encode(Format))
        D = D + 1  
    else:
        conn.sendall(KHL.encode(Format))
    if D == 1:
        conn.sendall(C.encode(Format))
    while D == 1:

        time.sleep(0.01)
        Chat = input("Chat: ")
        AD = "Admin:"
        Chat = AD + Chat + "\n" 
        conn.send(Chat.encode(Format))
        try:
            MSG = conn.recv(1000).decode(Format)
            print(MSG)
        except:
            time.sleep(0.01)
except:
    print("Client Đã ngưng kết nối vui lòng thử lại!(Phần mềm sẽ tự động dừng trong 10 giây)")
    time.sleep(10)

else:
    conn.sendall(KC.encode(Format))
    print(KC)

