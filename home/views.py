from django.http import HttpResponse
import os

# Create your views here.
def home(request):
    ENVIRONMENT = os.getenv('APP_ENV')
    return HttpResponse(f"Welcome to the Home Page! (Environment: {ENVIRONMENT})")
