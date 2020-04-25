from django.shortcuts import render
from .models import Profile, Submission
from .forms import Submit
# Create your views here.

def index(request):
    context = {"submitform": Submit}
    return render(request, 'photocontest/index.html', context=context)

    if (request.method == "POST"):
        #new submission added