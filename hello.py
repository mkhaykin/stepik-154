#! /usr/bin/python
#

def hello(environ, start_response):
    query = environ['QUERY_STRING'].strip('/?').split('&')
    # query = '/?a=1&a=2&b=3'.strip('/?').split('&')
    # s = '\n'.join(query)
    # data = s.encode('utf-8')

    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return query

