from rest_framework import serializers
from .models import*
from OpsUser.models import OpsUser

class SignupClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = ClientSignup
        fields = ('id','email','otp_verified')
        extra_kwargs = {'password': {'write_only': True}}

class ShowFilesSerializers(serializers.ModelSerializer):
    # snippets = serializers.PrimaryKeyRelatedField(many=True,queryset=OpsUser.objects.all())
    class Meta:
        models = OpsUser
        # fields = "__all__"
        fields = ('id', 'uploaded_by', 'upload_file')

# class VerifySerializers(serializers.ModelSerializer):
#     class Meta:
#         mod