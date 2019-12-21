from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import UserRegisterForm,CandidateDetailsForm
from .models import Candidate,Challenge,Question,Candidate_codes
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from datetime import datetime,timedelta
from django.http import HttpRequest
from django.views.generic import CreateView
from django.contrib.auth import authenticate
from . tokens import account_activation_token
from django.http import HttpRequest
from django.http import HttpResponse
import json,time
import smtplib
from django.db.models import Q
from django.utils import timezone
from .compile_run_api import compile_run
def home(request):
    if request.user.is_authenticated:
        return redirect('tests')
    return render(request,'challenge/home.html.',{
'header':'Host Analytics Exam Platform',
'title':'HA Exam',
})


def challenges(request):
    context ={
        'challenges':Challenge.objects.all()
    }
    return render(request,'challenge/challenges.html',context)

def test_instruction(request,pk,c_id):
    challenge = Challenge.objects.get(pk=pk)
    candidate = Candidate.objects.get(pk=c_id)
    return render(request,'challenge/test_instruction.html',{'challenge':challenge,'candidate':candidate})

def candidate_form(request,challenge_id):
    test = Challenge.objects.get(pk=challenge_id)
    candidate = Candidate.objects.filter(user=request.user)
    print(candidate)
    if candidate.filter(test_name= test).first() is None:
        if request.method == "POST":
            form= CandidateDetailsForm(request.POST,request.FILES)
            if form.is_valid():
                form.instance.user = request.user
                form.instance.test_name = test
                form.save()
                return redirect('test_instruction',pk=challenge_id,c_id=form.instance.id)     
        else:
            form= CandidateDetailsForm()
        return render(request,'challenge/candidate_details.html',
                                {'form':form}
                                )
    else:
        c = candidate.filter(test_name = test).first()
        return redirect('test_instruction',pk=challenge_id,c_id=c.id)

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
    {'form':form},)

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

def testpage(request,challenge_id,c_id):
    challenge = Challenge.objects.get(pk=challenge_id)
    candidate = Candidate.objects.get(pk=c_id)
    print(candidate)
    questions = Question.objects.filter(challenge=challenge)
    candidate_codes_obj = Candidate_codes.objects.filter(candidate=candidate)
    c= candidate.count
    candidate.count = c+1
    candidate.save()

    if candidate.count<=1:
        duration = challenge.Test_Duration
        candidate.start_time=datetime.now()
        candidate.end_time=datetime.now()+timedelta(minutes=duration)
        candidate.save()
        for q in questions:
            candidate_code = Candidate_codes(question=q,candidate=candidate)
            candidate_code.save()
    
    if request.is_ajax() and request.method == "POST" :
        code_output=""
        if request.POST.get('compile_run') == 'yes':
            code_output = save_run(request,candidate_codes_obj)
            res={'msg':code_output}
            return HttpResponse(json.dumps(res), content_type="application/json")
        if request.POST.get('question') == 'yes':
            q_id = request.POST.get('q_id')
            question = Question.objects.get(pk=q_id)
            candidate_question_code =""
            candidate_codes_obj = Candidate_codes.objects.filter(candidate=candidate)
            for i in candidate_codes_obj:
                if i.question.id is question.id:
                    candidate_question_code = i
            return question_codes(candidate_question_code)    
    return render(request,'challenge/testpage.html',{'challenge':challenge,'questions':questions,'candidate':candidate,'candidate_codes':candidate_codes_obj,})

def save_run(request,candidate_codes_obj):
    q_id = request.POST.get('q_id')
    question = Question.objects.get(pk=q_id)
    language = request.POST.get('language')
    code = request.POST.get('code')
    custom_input = request.POST.get('input')
    candidate = candidate_codes_obj.first().candidate
    save_codes(candidate_codes_obj,code,language,question)
    code_output = compile_run(language,code,custom_input,request,candidate)
    print("***compile_run",code_output)
    return code_output
  
def save_codes(candidate_codes_obj,code,language,question):
    candidate_question_code=""
    for i in candidate_codes_obj:
        if i.question.id is question.id:
            candidate_question_code = i
            break    
    print("saving question")
    if language == "Python":
        candidate_question_code.python_code=code
        candidate_question_code.save()
    elif language == "C":
        candidate_question_code.c_code=code
        candidate_question_code.save()
    elif language == "C++":
        candidate_question_code.cpp_code=code
        candidate_question_code.save()
    elif language == "Java":
        candidate_question_code.java_code=code
        candidate_question_code.save()
    elif language == "C#":
        candidate_question_code.csharp_code=code
        candidate_question_code.save()  

def question_codes(candidate_question_code):
    codes = {
        'python':candidate_question_code.python_code,
        'java':candidate_question_code.java_code,
        'csharp':candidate_question_code.csharp_code,
        'cpp':candidate_question_code.cpp_code,
        'c':candidate_question_code.c_code,
    }
    print(codes)
    return HttpResponse(json.dumps(codes), content_type="application/json")