
import socket
import time
try:
    A = 0
    D = 0
    DNHL = "Đăng nhập hợp lệ"
    DNHL = str(DNHL)

    Host = "127.168.1.209"
    Port = 60432
    Format = "utf32"

    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    print("client side")

    s.connect( (Host, Port) )
    print("Địa chỉ Client:",s.getsockname())
    #Đăng nhâp
    user = input("Username: ")
    password = input("Password: ")

    s.sendall(user.encode(Format))
    s.sendall(password.encode(Format))
    TH = s.recv(100).decode(Format)
    print(TH)
    #nhận tin
    while TH == "Đăng nhập hợp lệ":
        Chat = input("Chat: ")
        Chat = user + ": " + Chat  + "\n"
        s.sendall(Chat.encode(Format))
        time.sleep(00.1)
        MSG = s.recv(1000).decode(Format)
        print(MSG)
except:
    print("Phần mềm không thể kết nối được với Máy chủ!\nVui lòng thử lại(Phần mềm sẽ tự động dừng trong 10 giây)")
    time.sleep(10)


