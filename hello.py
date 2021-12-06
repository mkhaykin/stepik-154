#! /usr/bin/python
#

def app(environ, start_response):
    query = environ['QUERY_STRING'].strip('/?').split('&')
    # s = '\n'.join(query)
    s = '\n'.join(['a=a', 'b=b'])
    if not s:
        s = 'no data'

    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain')
        ('Content-Length', str(len(s)))
    ]
    start_response(status, response_headers)
    return iter([bytes(s, 'utf-8')])


def test_ok(environ, start_response):
    """Simplest possible application object"""
    data = b'Hello, World!\n'
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])