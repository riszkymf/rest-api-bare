from http.server import  BaseHTTPRequestHandler
from libs import payload_handler,response_handler
import json
from random import randint


class ServiceHandler(BaseHTTPRequestHandler):
    route = '/api/payload'
	
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type','text/json')
        length = int(self.headers['Content-Length'])
        content = self.rfile.read(length)
        temp = str(content).strip('b\'')
        self.end_headers()
        return temp
	
    def do_GET(self):
        if self.path != self.route:
            self.send_response(404,"Address not found")
            self.send_header('Content-type','text/json')
            self.end_headers()
            response = response_handler.get_response(
                data={},
                status_code=404,
                message="Address not founds"
            )
        else:
            self.send_response(200)
            self.send_header('Content-type','text/json')
            self.end_headers()
            data = payload_handler.generate_payload()
            response = response_handler.get_response(200,data,"Success")
        self.wfile.write(response.encode())

    def do_PUT(self):
        if self.path != self.route:
            self.send_response(404,"Address not found")
            self.send_header('Content-type','text/json')
            self.end_headers()
            response = response_handler.get_response(
                data={},
                status_code=404,
                message="Address not founds"
            )
            self.wfile.write(response.encode())
            return      
        content_length = int(self.headers['Content-Length'])
        if not content_length:
            self.send_response(400,"Invalid input")
            self.send_header('Content-type','text/json')
            self.end_headers()
            response = response_handler.get_response(
                data={},
                status_code=400,
                message="Invalid JSON Input"
            )
            self.wfile.write(response.encode())
            return
        try:
            input_json = self.rfile.read(content_length)
            input_data = json.loads(input_json)
        except Exception as e:
            print(str(e))
            self.send_response(400,"Malformed Input")
            self.send_header('Content-type','text/json')
            self.end_headers()
            response = response_handler.get_response(
                data={},
                status_code=400,
                message="Malformed Input. Please enter valid json"
            )
            self.wfile.write(response.encode())
            return
        else:
            self.send_response(200)
            self.send_header('Content-type','text/json')
            self.end_headers()
            input_data.update({"job_number": randint(0,100)})
            response = response_handler.get_response(
                data=input_data,
                status_code=200,
                message="Success"
            )
            self.wfile.write(response.encode())

            


