#!/usr/bin/python3
# -*- coding: utf-8 -*-
import ask
import sendRequest
import getRequest
import getResponse
import sendResponse
import xml.etree.ElementTree as etree


from http.server import BaseHTTPRequestHandler, HTTPServer


# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)
        print('Принят GET запрос')
        # Send headers
        self.send_header('Content-type', 'text/xml;charset=utf-8')
        self.end_headers()

        # Send message back to client
        message = ""
        with open('Шаблоны/wsdl.xml', mode='r', encoding='utf-8') as fp:
            message = fp.read()
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf-8"))
        print('Вернуль WSDL')
        return

    def do_POST(self):
        # Send response status code
        self.send_response(200)
        cl = int(self.headers['Content-Length'])
        sa = self.headers['SOAPAction']
        message = "Hello world!"

        post_body = self.rfile.read(cl).decode('utf-8')
        xml_tree = etree.fromstring(post_body)
        """По неизвестной мне причине Вадим не передает soapaction, поэтому эмулятор делаю с поиском по дереву
        xml. Ведь это намного проще, отпарсить дерево, чем soapaction!!!"""
        if not sa:
            if xml_tree.find('{http://schemas.xmlsoap.org/soap/envelope/}Body/'
                             '{urn://x-artefacts-smev-gov-ru/services/message-exchange/types/1.1}GetRequestRequest'):
                sa = '"urn:GetRequest"'
            elif xml_tree.find('{http://schemas.xmlsoap.org/soap/envelope/}Body/'
                               '{urn://x-artefacts-smev-gov-ru/services/message-exchange/types/1.1}AckRequest'):
                sa = '"urn:Ack"'
            elif xml_tree.find('{http://schemas.xmlsoap.org/soap/envelope/}Body/'
                               '{urn://x-artefacts-smev-gov-ru/services/message-exchange/types/1.1}SendResponseRequest'):
                sa = '"urn:SendResponseRequest"'

        print('Метод:', sa)
        if sa == '"urn:Ack"':
            print("Принят запрос ACK - подтверждение приема")
            message = ask.get_ask()
        elif sa == '"urn:SendRequest"':
            print('Принял SendRequest - отправка ответа')
            message = sendRequest.send_request(post_body)
        elif sa == '"urn:GetRequest"':
            print('Принял GetRequest - получение запросов к нам')
            message = getRequest.get_request()
        elif sa == '"urn:GetResponse"':

            message = getResponse.get_response(post_body)
        elif sa == '"urn:SendResponseRequest"':
            print('Принял SendResponse - отправка ответа')
            message = sendResponse.send_response(post_body)

        # Send headers
        self.send_header('Content-type', 'text/xml;charset=utf-8')
        self.end_headers()

        # Send message back to client

        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf-8"))
        return


def run():
    print('starting server...')

    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    server_address = ('0.0.0.0', 8081)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()

run()

