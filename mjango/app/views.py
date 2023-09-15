from django.shortcuts import render
from random import randint
from django.views import View

class Index(View):
    def get(self,request):
        context = {'titel': 'MJANGO - M1 Server'}
        return render(request, 'app/index.html', context)
