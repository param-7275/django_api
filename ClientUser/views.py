from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.mail import send_mail
from .models import*
from .serializers import*
from .serializers import*
from rest_framework.views import APIView
from django.contrib.auth import login,logout,authenticate
from django.views.decorators.csrf import csrf_exempt
from OpsUser.serializers import SerializersFileData
from .email_verify import*
csrf_exempt


# Create your views here.

class ClientSignup(APIView):
     def post(self,request):
        try:
            postdata = SignupClientSerializers(data=request.data)
            if postdata.is_valid():
                send_mail(postdata.data['email'])
                postdata.save()
            context = {
            'sucess': True,
            'status' : status.HTTP_200_OK,
            'response': postdata.data
                        }
            return Response(context,status=status.HTTP_200_OK)
        except Exception as E:
            context = {
                'sucess': False,
                'status' : status.HTTP_400_BAD_REQUEST,
                'response': str(E)
                }
            return Response(context,status.HTTP_400_BAD_REQUEST)

class ClientLogin(APIView):
    def post(self,request):
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            myuser = authenticate(username=username,password=password)
            if myuser:
                login(request,myuser)
            context = {
            'sucess': True,
            'status' : status.HTTP_200_OK,
            'response': 'login sucessfully'
                        }
            return Response(context,status=status.HTTP_200_OK)
        except Exception as E:
            context = {
                'sucess': False,
                'status' : status.HTTP_400_BAD_REQUEST,
                'response': str(E)
                }
            return Response(context,status.HTTP_400_BAD_REQUEST)
        
class ShowFiles(APIView):
    def get(self,request):
        try:
            showdata = OpsUser.objects.all() 
            serializer = SerializersFileData(showdata, many =True)
            context = {
                'sucess': True,
                'status' : status.HTTP_200_OK,
                'response': serializer.data
            }
            return Response(context,status=status.HTTP_200_OK)
        except Exception as E:
            context = {
                'sucess': False,
                'status' : status.HTTP_400_BAD_REQUEST,
                'response': str(E)
                }
            return Response(context,status.HTTP_400_BAD_REQUEST)
        


class Verify_otp(APIView):
    def post(self,request):
        try:
            serializer = SignupClientSerializers(data=request.data)
            if serializer.is_valid():
                email = serializer.data['email']
                otp = serializer.data['otp']
                user = ClientSignup.objects.filter(email=email)
                send_mail(serializer.data['email'])
                serializer.save()
                if not user.exists():
                    return Response(
                        {
                            'sucess': False,
                            'status' : status.HTTP_400_BAD_REQUEST,
                            'message': 'invalid email'
                        }
                    )
                if not user[0].otp == otp:
                    return Response(
                        {
                            'sucess': False,
                            'status' : status.HTTP_400_BAD_REQUEST,
                            'message': 'wrong otp'
                        }
                    )
                user = user.first()
                user.is_verified = True
                user.active = True
                user.save()
                
                return Response({
                    'status':200,
                    'message':'Account Verified Successfully.',
                    'data': {},
                })

        
        except Exception as E:
            print(str(E))