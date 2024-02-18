from django.shortcuts import render


# Create your views here.
def main(request):
    return render(request, 'quoteapp/index.html')

def author(request):
    return render(request, 'quoteapp/author/Albert Einstein.html')