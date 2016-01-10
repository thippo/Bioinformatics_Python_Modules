def domain_to_ip(domain):
    import socket
    return socket.getaddrinfo(domain, None)[0][4][0]