from http.server import HTTPServer
from route import ServiceHandler
import argparse





if __name__ == '__main__':
    usage = ''' python3 server.py [--help] [-p PORT_NUMBER]'''
    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument("-p","--port",action="store",type=int,help="PORT NUMBER (Must be integer between 1025-65536). Default 8080")
    args = parser.parse_args()
    if not args.port:
        port = 8080
    else:
        port = args.port
    print("Running REST Service on http://0.0.0.0:{}".format(port))
    Handler = ServiceHandler
    server = HTTPServer(('0.0.0.0',port),Handler)
    while True:
        try:
            server.serve_forever()
        except Exception as e:
            print("Server Error : ", str(e))
            print("Restarting REST Service on http://0.0.0.0:{}".format(port))
            server.serve_forever()