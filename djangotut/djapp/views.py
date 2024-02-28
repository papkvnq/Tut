from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def app(request):
    return HttpResponse("Yo Paps!")

def appabt(request):
    return HttpResponse("Ask about me")