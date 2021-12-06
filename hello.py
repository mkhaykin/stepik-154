#! /usr/bin/python
#

def hello(environ, start_response):
    query = environ['QUERY_STRING'].strip('/?').split('&')
    # data = [bytes(s + '\n', 'ascii') for s in query]
    s = '\n'.join(query)
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain')  # ,
        # ('Content-Length', str(len(s)))
    ]
    start_response(status, response_headers)
    if s:
        return iter([bytes(s, 'utf-8')])
    else:
        return item([bytes('no data', 'utf-8')])

def app(environ, start_response):
    """Simplest possible application object"""
    data = b'Hello, World!\n'
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])