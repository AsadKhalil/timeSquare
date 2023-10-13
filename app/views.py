from django.shortcuts import render

# Create your views here.


def home_view(request):
    context = { "ASAD": "ASAD"}
    return render(request, 'home.html', context)


def about_view(request):
    context = { "ASAD": "ASAD"}
    return render(request, 'about.html', context)


def services_view(request):
    context = { "ASAD": "ASAD"}
    return render(request, 'about.html', context)


def web_development_view(request):
    context = { "ASAD": "ASAD"}
    return render(request, 'web.html', context)


def app_development_view(request):
    context = { "ASAD": "ASAD"}
    return render(request, 'app.html', context)

def seo_services_view(request):
    context = { "ASAD": "ASAD"}
    return render(request, 'seo.html', context)

def ppc_management_view(request):
    context = { "ASAD": "ASAD"}
    return render(request, 'ppc.html', context)

def social_media_marketing_view(request):
    context = { "ASAD": "ASAD"}
    return render(request, 'smm.html', context)

def content_marketing_view(request):
    context = { "ASAD": "ASAD"}
    return render(request, 'cmm.html', context)

def cyber_security_view(request):
    context = { "ASAD": "ASAD"}
    return render(request, 'cyber.html', context)

def careers_view(request):
    context = { "ASAD": "ASAD"}
    return render(request, 'careers.html', context)

def blog_view(request):
    context = { "ASAD": "ASAD"}
    return render(request, 'blog.html', context)


def contact_view(request):
    context = { "ASAD": "ASAD"}
    return render(request, 'contact.html', context)



def terms_view(request):
    context = { "ASAD": "ASAD"}
    return render(request, 'terms.html', context)



def privacy_view(request):
    context = { "ASAD": "ASAD"}
    return render(request, 'privacy.html', context)