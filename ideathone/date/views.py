from django.shortcuts import redirect, render

# Create your views here.
def calendar(request):
    return render(request, "calendar.html")