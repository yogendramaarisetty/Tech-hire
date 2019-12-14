from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import UserRegisterForm,CandidateDetailsForm
from .models import Candidate,Challenge
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from datetime import datetime
from django.http import HttpRequest
from django.views.generic import CreateView
from django.contrib.auth import authenticate
from . tokens import account_activation_token
from django.http import HttpRequest
from django.http import HttpResponse
import json,time
import smtplib
from django.db.models import Q
def home(request):
    if request.user.is_authenticated:
        return redirect('tests')
    return render(request,'challenge/home.html.',{
'header':'Host Analytics Exam Platform',
'title':'HA Exam',
})
def index(request):
    return render(request,'challenge/index.html')
def challenges(request):
    print(request.user.username)
    context ={
        'challenges':Challenge.objects.all()
    }
    return render(request,'challenge/challenges.html',context)

def test_instruction(request):
    challenge = request.user.candidate.test_name
    return render(request,'challenge/test_instruction.html',{'challenge':challenge})

def candidate_form(request,challenge_id):
    test = None
    if Candidate.objects.all().filter(user=request.user).first() is None:
        print("this is none")
        if request.method == "POST":
            form= CandidateDetailsForm(request.POST,request.FILES)
            if form.is_valid():
                form.instance.user = request.user
                test = Challenge.objects.get(pk=challenge_id)
                form.instance.test_name = test
                form.save()
                return redirect('test_instruction')     
        else:
            form= CandidateDetailsForm()
        return render(request,'challenge/candidate_details.html',
                                {'form':form},
                                {
                                    'title':'Host Analytics Hiring',
                                    'header':'Host Analytics Exam'
                        })
    else:
        return redirect('test_instruction')
    
   
        

    return render(request,'challenge/candidate_form.html',{'challenge_id':challenge_id})

def challenge_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            rollnumber = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password1')
            user = User.objects.all().filter(username=rollnumber).first()
            form.is_active = False
            current_site = get_current_site(request)
            subject = 'Activate Your your test'
            message = render_to_string('challenge/account_activation_email.html', {
                'user': form,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })           
            messages.success(request, f'Your test registration Link is sent to {email}.')
            send_email(subject, message, user)
            return redirect('account_activation_sent')
    else:
        form = UserRegisterForm()
    return render(request,'challenge/register.html',
    {'form':form},
    {
        'title':'Host Analytics Hiring',
        'header':'Host Analytics Exam'
    })

def account_activation_sent(request):
    return render(request, 'challenge/account_activation_sent.html')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('tests')
    else:
        return render(request, 'challenge/account_activation_invalid.html')
#SMTP for senting email
def send_email(subject, msg, user):
    to="167r1a05m4@gmail.com"
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login("yogendramaarisetty@gmail.com", "yyyooogggiii1")
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail("yogendramaarisetty@gmail.com", user.email, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")