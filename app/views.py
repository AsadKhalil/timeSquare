from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

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





@csrf_exempt
def contact_form_submission(request):
    if request.method == "POST":
        help_option = request.POST.get("help")
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        organization = request.POST.get("organization")
        description = request.POST.get("description")
        subscribe = request.POST.get("subscribe")

        # Build email content
        email_subject = "New Contact Form Submission"
        email_body = f"""
            Help: {help_option}
            Name: {name}
            Email: {email}
            Phone: {phone}
            Organization: {organization}
            Description: {description}
            Subscribe: {'Yes' if subscribe else 'No'}
        """

        # Send the email
        send_mail(
            email_subject,
            email_body,
            'eli@timesquarellc.com',  # This is the sender's email',  # Replace with your sender's email address
            ['eli@timesquarellc.com'],  # Replace with your email address where you want to receive the form submissions
            fail_silently=False,
        )

        return redirect('/')

    return redirect('/')
