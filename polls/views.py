from django.http import HttpResponse 
def index(request): 
	return HttpResponse("Hello, djangorgeous. Nice to meet you. You're at the polls index.")