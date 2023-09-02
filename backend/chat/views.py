from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from rest_framework.generics import ListCreateAPIView
from .serializers import *
# @csrf_exempt
# def send_message(request):
#     if request.method == 'POST':
#         print(request.POST)
#         import pdb
#         pdb.set_trace()
#         message = request.POST.get('message')
#         print(message)
#         if message:
#             new_message = Message.objects.create(content=message)
#             return JsonResponse({'status': 'success', 'message': new_message.content})
#         else:
#             return JsonResponse({'status': 'error', 'message': 'Message cannot be empty.'})
#     else:
#         return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})
#
# def get_messages(request):
#     messages = Message.objects.all().order_by('-created_at')[:10]
#     message_list = [{'content': message.content, 'created_at': message.created_at} for message in messages]
#     return JsonResponse({'messages': message_list})

class MessageListView(ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer