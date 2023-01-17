import socket, time, os

def proxy(conn: socket.socket):
    google_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    google_s.connect((socket.gethostbyname('www.google.com'), 80))
    print('connected to www.google.com')

    client_data = conn.recv(4096)

    google_s.sendall(client_data)
    google_s.shutdown(socket.SHUT_WR)

    full_data = bytearray()
    while True:
        data = google_s.recv(4096)
        if data:
            full_data.extend(data)
        else:
            break

    time.sleep(10)

    conn.sendall(full_data)
    conn.shutdown(socket.SHUT_WR)

    google_s.close()
    conn.close()


def main():
    client_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_s.bind(('127.0.0.1', 8080))
    client_s.listen(2)
    print('listening to port 8080')

    while True:
        conn, addr = client_s.accept()
        if os.fork() == 0:
            print('connected to', addr)
            proxy(conn)
            break

if __name__ == "__main__":
    main()
