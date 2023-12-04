
from rest_framework import  status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.mail import send_mail
from .models import*
from .serializers import*
from .serializers import*
from rest_framework.views import APIView
from django.contrib.auth import login,authenticate
from .validate import validate_file_extension

# Create your views here.


class OpsUploadFiles(APIView):
    def post(self,request):
        try:
            postdata = SerializersFileData(data = request.data)
            if validate_file_extension:
                if postdata.is_valid():
                    postdata=OpsUser.objects.create(postdata)
                    postdata.save()
                    context = {
                        'sucess': True,
                        'status' : status.HTTP_201_CREATED,
                        'response': 'file upload sucesssfully'
                    }
                    return Response(context,status=status.HTTP_201_CREATED) 
                context = {
                    'sucess': False,
                    'status' : status.HTTP_400_BAD_REQUEST,
                    'response': "File type not supported. Allowed types: pptx, docx, xlsx"
                    }
                return Response(context,status.HTTP_400_BAD_REQUEST)

        except Exception as E:
            context = {
                'sucess': False,
                'status' : status.HTTP_400_BAD_REQUEST,
                'response': str(E),
                
                }
            return Response(context,status.HTTP_400_BAD_REQUEST)
        
class OpsSignUp(APIView):
    def post(self,request):
        try: 
            postdata = SignupOps(data=request.data)
            print(postdata)
            if postdata.is_valid():
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

class OpsLogin(APIView):
    def post(self,request):
        try:
            username = request.data.get('username')
            print(username)
            password = request.data.get('password')
            print(password)
            myuser = authenticate(username=username,password=password)
            print(myuser)
            if myuser is not None:
                
                login(request,myuser)
                print(myuser)
                context = {
                'sucess': True,
                'status' : status.HTTP_200_OK,
                'response': 'login sucessfully'
                            }
                return Response(context,status=status.HTTP_200_OK)
            else:
                context = {
                'sucess': False,
                'status' : status.HTTP_400_BAD_REQUEST,
                'response': 'fhjfh'
                }

        except Exception as E:
            context = {
                'sucess': False,
                'status' : status.HTTP_400_BAD_REQUEST,
                'response': str(E)
                }
            return Response(context,status.HTTP_400_BAD_REQUEST)
            

