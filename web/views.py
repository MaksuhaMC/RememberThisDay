from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'RTDaylist.html')

def about(request):
    return HttpResponse('<h1>This is About page</h1>')

# def reverse(request):
#     usertext = request.GET['usertext']
#     reversedtext = usertext[::1]
#     word_counter = len(usertext.split())
#     context = {
#         'usertext': usertext,
#         'reversedtext': reversedtext,
#         'word_counter': word_counter
#     }
#     return render(request, 'web/reverse.html', context=context)

def homepage(request):
    return render('<h1>Возврат на главную страницу</h1>')
