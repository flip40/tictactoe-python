from django.shortcuts import render

# Create your views here.
def chat(request):
#         alerts_list = Alert.objects.all()
        context = {}
        return render(request, 'chat/chat.html', context)