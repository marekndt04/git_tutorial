from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class MainView(View):
    def get(self, request):
        return HttpResponse('Hello world !')


class MasterView(View):
    def get(self, request):
        return HttpResponse('Master makes hellO world to You :* also changed')


class TestView(View):
    def get(self, request):
        user = request.user
        return HttpResponse(f'Test branch makes hello world to {user} ;P')

