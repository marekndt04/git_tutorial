from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class MainView(View):
    def get(self, request):
        return HttpResponse('Hello world !')


class MasterView(View):
    def get(self, request):
        pass


class TestView(View):
    pass