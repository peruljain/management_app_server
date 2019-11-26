from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets,generics,permissions
from management.models import *
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from rest_framework.authtoken.models import Token
from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.shortcuts import redirect
from django.core.mail import send_mail,EmailMessage
from random import randint

class Welcome(APIView):
    """ 
    This class shows a welcome message on starting of app
    """
    permission_classes=(permissions.AllowAny,)
    def get(self,request,*args,**kwargs):
        return JsonResponse({
            "success":True,
        })

class CheckIn(APIView):
    permission_classes=(permissions.AllowAny,)
    authentication_classes=(TokenAuthentication,)
    def post(self,request,*args,**kwargs):
        v_name=request.POST.get('visitor_name')
        v_email=request.POST.get('visitor_email')
        v_phone=request.POST.get('visitor_phone')
        h_name=request.POST.get('host_name')
        h_email=request.POST.get('host_email')
        h_phone=request.POST.get('host_phone')
        now=datetime.datetime.now().time()
        time = now.strftime("%H:%M:%S")
        if User.objects.filter(username=v_email).count!=0:
            try:
                user=User.objects.get(username=v_email)
                data=Database.objects.get(user=user)
                data.visitor_name=v_name
                data.visitor_phone=v_phone
                data.host_name=h_name
                data.host_phone=h_phone
                data.host_email=h_email
                data.time=time
                data.save()
            except:
                pass

            
            
        else :
            user=User.objects.create_user(username=v_email,password=v_email,email=v_email)
            data=Database.objects.get(user=user)
            data.visitor_name=v_name
            data.visitor_phone=v_phone
            data.host_name=h_name
            data.host_phone=h_phone
            data.host_email=h_email
            data.time=time
            data.save()
        subject='Appointment'
        message= 'name : '+ v_name + '\n'+'email : '+ v_email + '\n'+'Phone : '+ v_phone + '\n'+'CheckInTime : '+ time + '\n'         
        temail=EmailMessage(subject,message,to=[h_email])
        temail.send()
        return JsonResponse({
            'success':True
        })

class CheckOut(APIView):
    permission_classes=(permissions.AllowAny,)
    def post(self,request,*args,**kwargs):
        v_email=request.POST.get('visitor_email')
        user=User.objects.get(username=v_email)
        data=Database.objects.get(user=user)
        v_name=data.visitor_name
        v_phone=data.visitor_phone
        h_name=data.host_name
        h_email=data.host_email
        h_phone=data.host_phone
        check_in_time=data.time
        check_out_time=datetime.datetime.now().time()
        subject='Appointment'
        message='Dear '+v_email+'blah    '
        temail=EmailMessage(subject,message,to=[v_email])
        temail.send()
        return JsonResponse({
            'success':True
        })