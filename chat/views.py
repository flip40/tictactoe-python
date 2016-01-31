from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from models import Message

# Create your views here.
def chat(request):
#	alerts_list = Alert.objects.all()
	context = {}
	return render(request, 'chat/chat.html', context)

def update_chat(request):
	messages = Message.objects.all()
	return HttpResponse(serializers.serialize("json", messages), content_type="application/json")

@csrf_exempt
def send_message(request):
	if request.method == 'POST':
		if 'message' in request.POST:
			Message.objects.create(text=request.POST.get('message', 'Error: Message Not Received'))
	return HttpResponse("Message logged.", content_type="text/plain")
