# I have created this file - Milan
from django.http import HttpResponse

def index(request):
    return HttpResponse('''Hello, Milan <a href="https://www.instagram.com">Instagram</a>''')

def about(request):
    return HttpResponse("About Milan")