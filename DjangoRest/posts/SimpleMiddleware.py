
from django.http import HttpResponse,HttpRequest
from django.utils.deprecation import MiddlewareMixin

class AnotherMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        print('inside init of middleware...')
        self.get_response = get_response

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return self.get_response(request)

    def process_exception(self, request, exception):
        print('inside exeception')
        print(exception)
        return HttpResponse("in exception")

    def process_request(self, request):
        print('inside process request middleware')

    def process_response(self, request, response):
        print('process_response middleware...')
        return response