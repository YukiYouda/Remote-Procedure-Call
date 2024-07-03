import socket
import os
import json
import math

def subtract(x, y):
    return x - y

def floor(x):
    return math.floor(x)

def nroot(n, x):
    return math.pow(x, 1/n)

def reverse(s):
    return s[::-1]

def sort(strArr):
    return sorted(strArr)

def validAnagram(str1, str2):
    return sorted(str1) == sorted(str2)

functions = {
    'subtract' : subtract,
    'floor' : floor,
    'nroot' : nroot,
    'reverse' : reverse,
    'sort' : sort,
    'validAnagram' : validAnagram,
}

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = '/tmp/socket_file'

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print('Starting up on {}' .format(server_address))

sock.bind(server_address)

sock.listen(1)

while True:
    connection, cilent_address = sock.accept()
    try:
        print('connection from', cilent_address)

        while True:
            data = connection.recv(1024)
            data_json = json.loads(data.decode('utf-8'))

            if data:
                resonse = {}
                method = data_json['method']
                params = data_json['params']
                param_types = data_json['param_types']
                id = data_json['id']
                resonse['result_type'] = param_types[0]
                resonse['id'] = id

                if method == 'sort':
                    resonse['results'] = functions[method](params) 
                elif len(params) == 2:
                    resonse['results'] = functions[method](params[0], params[1]) 
                elif len(params) == 1:
                    resonse['results'] = functions[method](params[0]) 
                resonse =  json.dumps(resonse).encode('utf-8')
                connection.sendall(resonse)
            else:
                print('no data from', cilent_address)
                break
    finally:
        print('Closing current connection')
        connection.close()
