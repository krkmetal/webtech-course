from urlparse import parse_qs

def application(environ, start_response):
    results = ""
    status_code = '200 OK'
    response_headers = [('Content-type','text/plain')]
    parameters = parse_qs(environ["QUERY_STRING"], keep_blank_values=True)
    for parameter in parameters:
        parameter_data = "".join(parameters[parameter])
        results += "{}={}\n".format(parameter, parameter_data)
    start_response(status_code, response_headers)
    return [results]