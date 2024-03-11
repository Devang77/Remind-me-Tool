from django.shortcuts import render
from .models import reminder,remind_user
from .serializer import *
from django.http import JsonResponse
from django.contrib.auth import authenticate,login
from datetime import datetime
from django.conf import settings
from django.core.mail import EmailMessage
# from sendsms.message import SmsMessage
from sms import send_sms
def register_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        if username==None and password==None and email==None:
            return JsonResponse({'Message':'Please Provide Username,Password And Email','status':400})
        elif username==None:
            return JsonResponse({'Message':'Please Provide Username','status':402})
        elif password==None:
            return JsonResponse({'Message':'Please Provide Password','status':403})
        elif email==None:
            return JsonResponse({'Message':'Please Provide Email','status':405})
        else: 
            obj=remind_user.objects.create(username=username,password=password,email=email)
            reminder.objects.create(user_id=obj,email=email)
            return JsonResponse({'Message':'User Registered Successfully','status':200})
        
def user_login(request):
    if request.method == "POST":
        uname=request.POST.get('username')
        user_password=request.POST.get('password')
        
        # print(password,username,'llllllllllllllllllllll')
        if uname==None and user_password== None:
            return JsonResponse({'Message':'Please Provide Username And Password','status':401})
        elif uname==None:
            return JsonResponse({'Message':'Username Is Required','status':405})
        elif user_password==None:
            return JsonResponse({'Message':'Password Is Required','status':406})
        else:
            print('hiiiiiiiiiiiii')
            user=authenticate(request,username=uname,password=user_password)
            if user is not None:
                login(request,user)
                return JsonResponse({'Message':'Logged In Successfully','status':200})
            else:
                return JsonResponse({'Message':'Invalid Credentials','status':500})
def remind(request):
    if request.method=="POST":
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        reminder_description=request.POST.get('reminder_description')
        remind_date=request.POST.get('remind_date')
        date_obj=datetime.strptime(remind_date,'%d-%m-%Y')
        format_date=datetime.strftime(date_obj,'%Y-%m-%d')
        date=datetime.now()
        today_date=datetime.strftime(date,'%Y-%m-%d')
        reminder.objects.filter(email=email).update(reminder_description=reminder_description,remind_date=format_date)
        if today_date==format_date:
            subject=f"your reminder for {reminder_description}"
            message=f"Hey there!Just a quick heads up that you wanted to be reminded about {reminder_description} at {remind_date}. Time flies, so don't forget to take care of it when it pops up! 🕒If you've already handled it or need to reschedule, just let me know. I'm here to help!Best,"
            reciepent=[]
            reciepent.append(email)
            email_from=settings.EMAIL_HOST_USER
            msg=EmailMessage(subject=subject,body=message,from_email=email_from,to=reciepent)
            sent=msg.send()
            sms_msg=send_sms(f"Hey there!Just a quick heads up that you wanted to be reminded about {reminder_description} at {remind_date}. Time flies, so don't forget to take care of it when it pops up! 🕒If you've already handled it or need to reschedule, just let me know. I'm here to help!Best,","+918169580431",[phone])
            # print(sms_msg,'smsssssssssssssssssssssssssssss')
            # demo=sms_msg.send()
            
            if sent>0:
                reminder.objects.filter(email=email).update(reminder_status='Send')
                return JsonResponse({'Message':'Reminder send','status':200})            
            else:
                reminder.objects.filter(email=email).update(reminder_status='Not Send')
                return JsonResponse({'Message':'Reminder Is Not Send','status':405})
            
        else:
            return JsonResponse({'Message':'Reminder Is Due','status':300})