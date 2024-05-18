from django.shortcuts import render
from django.core.mail import send_mail
from core.models import GeneralSetting, Skill, Experience
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    site_title = GeneralSetting.objects.get(name='site_title').parameter
    site_keywords = GeneralSetting.objects.get(name='site_keywords').parameter
    site_description = GeneralSetting.objects.get(name='site_description').parameter
    About_desc = GeneralSetting.objects.get(name='About_desc').parameter
    About_me = GeneralSetting.objects.get(name='About_me').parameter
    About_me_desc = GeneralSetting.objects.get(name='About_me_desc').parameter
    About_me_desc2 = GeneralSetting.objects.get(name='About_me_desc2').parameter
    skills_desc = GeneralSetting.objects.get(name='skills_desc').parameter
    resume_desc = GeneralSetting.objects.get(name='resume_desc').parameter
    phone = GeneralSetting.objects.get(name='phone').parameter
    location = GeneralSetting.objects.get(name='location').parameter
    mail = GeneralSetting.objects.get(name='mail').parameter
    sumary_desc = GeneralSetting.objects.get(name='sumary_desc').parameter
    cert1_desc = GeneralSetting.objects.get(name='cert1_desc').parameter
    contact_desc = GeneralSetting.objects.get(name='contact_desc').parameter

    # Skills
    skills = Skill.objects.all()

    experiences = Experience.objects.all()

    context = {
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'About_desc': About_desc,
        'About_me': About_me,
        'About_me_desc': About_me_desc,
        'About_me_desc2': About_me_desc2,
        'skills_desc': skills_desc,
        'resume_desc': resume_desc,
        'phone': phone,
        'location': location,
        'mail': mail,
        'sumary_desc': sumary_desc,

        'cert1_desc': cert1_desc,
        'contact_desc': contact_desc,
        'skills': skills,
        'experiences': experiences
    }
    return render(request, 'index.html', context=context)


def contact(request):
    return render(request, 'index.html')


def contact_form(request):
    if request.method == 'POST':
        nameText = request.POST['name']
        emailText = request.POST['email']
        subjectText = request.POST['subject']
        messageText = request.POST['message']

        send_mail(
            "Message From :" + subjectText,
            f"Name: {nameText}\nEmail: {emailText}\n\n{messageText}",  # E-posta gövdesi
            'your-email@example.com',  # Gönderen e-posta adresi
            ['ferideyildirimer0@gmail.com'],  # Alıcı e-posta adresi
        )

        print("Form successfully submitted")
        return HttpResponseRedirect(reverse('index'))  # Redirect to the index page

    else:
        print("Form not submitted")
        return render(request, 'index.html', {"message_name": "hata"})
