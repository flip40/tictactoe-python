from django.shortcuts import render

def index(request):
	name = "clinton"
	return render(request, 'index/base.html', {'name': name})
