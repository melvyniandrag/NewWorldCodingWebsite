from django.shortcuts import render
from .forms import AstronomyBlogPostForm
from .models import AstronomyBlogPost
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, HttpResponseRedirect, HttpResponse

def home_view(request):
    context ={}
    return render(request, "mainapp/home_view.html", context) 


def coming_soon_view(request):
    context ={}
    return render(request, "mainapp/coming_soon_view.html", context) 

def teaching_view(request):
    context ={}
    return render(request, "mainapp/teaching_view.html", context) 


def horizon_view(request):
    context ={}
    return render(request, "mainapp/horizon_view.html", context) 


def workshop_webdevelopment_detail_view(request):
    context ={}
    return render(request, "mainapp/workshop_webdevelopment_detail_view.html", context) 


def workshop_textencoding_detail_view(request):
    context ={}
    return render(request, "mainapp/coming_soon_view.html", context) 


def workshop_arduinorobot_detail_view(request):
    context ={}
    return render(request, "mainapp/coming_soon_view.html", context) 


def workshop_gameboy_detail_view(request):
    context ={}
    return render(request, "mainapp/coming_soon_view.html", context) 


def workshop_introtokotlin_detail_view(request):
    context ={}
    return render(request, "mainapp/coming_soon_view.html", context) 
    

def workshop_introtolinux_detail_view(request):
    context ={}
    return render(request, "mainapp/coming_soon_view.html", context) 
    

def list_view(request):
    context ={}
    context["blog_posts"] = AstronomyBlogPost.objects.all().order_by('-id')
    return render(request, "mainapp/list_view.html", context) 


@login_required
def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = AstronomyBlogPostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/list")
         
    context['form']= form
    return render(request, "mainapp/create_view.html", context)
