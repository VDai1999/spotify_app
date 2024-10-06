from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
# def home(request):
#     return render(request, "spotify/test.html", {})
def home(request):
    template = loader.get_template('test.html')
    return HttpResponse(template.render())
