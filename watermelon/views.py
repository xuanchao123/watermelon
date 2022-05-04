from django.shortcuts import render, get_object_or_404
from .models import Information

# Create your views here.

def index(request):
    information_list = Information.objects.all().order_by('-created_time')
    return render(request, 'watermelon/index.html',   context={'information_list': information_list})

def detail(request):
    information = get_object_or_404(Information, pk=pk)
    return render(request, 'watermelon/detail.html', context={'information': information})