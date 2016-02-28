def application(environ, start_response):
    status_code = '200 OK'
    response_headers = [('Content-type','text/plain')]
    results = environ["QUERY_STRING"].replace('&','\n')
    start_response(status_code, response_headers)
    return [results]