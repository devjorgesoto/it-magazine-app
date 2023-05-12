from django.shortcuts import render

# Create your views here.
def home(request):

    # context and return
    context = {}
    return render(request, 'users/user.html', context)
