#! /usr/bin/python
#

def hello(environ, start_response):
    query = environ['QUERY_STRING'].strip('/?').split('&')
    data = [bytes(s + '\n', 'ascii') for s in query]

    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return data

