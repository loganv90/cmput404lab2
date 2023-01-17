import socket

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', 8080))
        print ('connected to proxy_server')

        payload = f'GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n'
        
        s.sendall(payload.encode())
        s.shutdown(socket.SHUT_WR)

        full_data = bytearray()
        while True:
            data = s.recv(4096)
            print("data:", data)
            if data:
                full_data.extend(data)
            else:
                break
        
        print(full_data)
    except Exception as e:
        print(e)
    finally:
        s.close()

if __name__ == "__main__":
    main()

