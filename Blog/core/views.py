# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse

def home(request):
	return render(request, "core/home.html")
def contact(request):
	return HttpResponse("<h1>Contact<h1>")
def cd(request):
	return HttpResponse("<h1>cd<h1>")
def portfolio(request):
	return HttpResponse("<h1>portfolio<h1>")
# Create your views here.
