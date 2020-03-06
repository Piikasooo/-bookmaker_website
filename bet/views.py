from django.shortcuts import render


def get_all(request):
    return render(request, 'bet/index.html')
