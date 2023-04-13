#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from PIL import Image, ImageDraw
import json
from base64 import b64decode, b64encode
from io import BytesIO
import pytesseract

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        #self._set_headers()
        print("\n\n--------------------\n\n")
        print(self.headers)
        print("\n\n--------------------\n\n")
        bbb = json.loads(post_data.decode())['image']
        #print(json.loads(post_data.decode())['image'])
        image = BytesIO(b64decode(bbb))
        #print(image)
        #with Image.open(image) as im:
        #    im.rotate(45).show()
        im = Image.open(image)
        size = im.size

        print('got')
        #print("ZZZZZZZZ  :  ", pytesseract.image_to_string(im, lang='jpn'))
        print("ZZZZZZZZ  :  ", pytesseract.image_to_boxes(im, lang='jpn'))
        print("2222")

        tt = Image.new('RGBA', size, (255, 0, 0, 0))
        #uu = ImageDraw.Draw(tt)
        #uu.ellipse((25, 25, 75, 75), fill=(255, 0, 0))

        #tt.save('test_tt.png', 'PNG')
        


        #im.rotate(45).show()
        #im.rotate(45)
        #cc = im.tobytes(encoder_name='raw')
        #dd = b64encode(im.tobytes(encoder_name='PNG'))
        mm = BytesIO()
        #mm.write(b"Some codded message")
        #im.save(mm, format='png')
        tt.save(mm, format='png')
        mm.seek(0)
        #print(mm)
        oo = b64encode(mm.read())
        #print(oo)
        pp = oo.decode('utf-8')
        #print(pp)
        #ee = dd.decode('utf-8')
        ff = {'image': pp}
        #ff = {'image': b64encode(image.read()).decode('utf-8')}
        jj = json.dumps(ff)
        output = jj.encode('utf-8')
        
        print("\n\n--------------------\n\n")
        print(parse_qs(urlparse(self.path).query))

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Content-Length", len(output))
        self.end_headers()
        #print("OUTPUT: ", output)
        self.wfile.write(output)
        #self.wfile.write(jj)

def run(server_class=HTTPServer, handler_class=S, port=4404):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
