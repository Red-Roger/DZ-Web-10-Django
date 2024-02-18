from django.shortcuts import render


# Create your views here.
def main(request):
    return render(request, 'quoteapp/index.html')

def AlbertEinstein(request):
    return render(request, 'quoteapp/author/Albert Einstein.html')


def JKRowling(request):
    return render(request, 'quoteapp/author/J.K. Rowling.html')


def JaneAusten(request):
    return render(request, 'quoteapp/author/Jane Austen.html')


def ThomasMann(request):
    return render(request, 'quoteapp/author/Thomas Mann.html')


def MarilynMonroe(request):
    return render(request, 'quoteapp/author/Marilyn Monroe.html')


def AndréGide(request):
    return render(request, 'quoteapp/author/André Gide.html')


def ThomasAEdison(request):
    return render(request, 'quoteapp/author/Thomas A. Edison.html')


def EleanorRoosevelt(request):
    return render(request, 'quoteapp/author/Eleanor Roosevelt.html')


def SteveMartin(request):
    return render(request, 'quoteapp/author/Steve Martin.html')

