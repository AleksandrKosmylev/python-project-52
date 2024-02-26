from django.shortcuts import render


# Create your views here.
def main_statuses(request):
    return render(request, 'statuses/statuses.html')
