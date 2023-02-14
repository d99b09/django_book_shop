from rest_framework import generics, permissions
from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.settings import api_settings


from userprofiles.models import UserProfile
from userprofiles.serializers import UserProfileSerializer



class UserProfileList(generics.ListCreateAPIView):
    # schema = AutoSchema(tags=['User profiles'])
    permission_classes = (permissions.IsAuthenticated, )
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    http_method_names = ['get']


class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    # schema = AutoSchema(tags=['User profiles'])
    lookup_field = 'uuid'
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    # schema = AutoSchema(tags=['User profiles'])
    @classmethod
    def get_token(cls, user):
        # data = {}
        data = super().get_token(user)

        # Add custom claims
        data['uuid'] = str(user.profiles.uuid)
        # # ...
        # data['access'] = token['access']
        # data['refresh'] = token['refresh']
        return data

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['uuid'] = str(refresh.payload['uuid'])

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    # schema = AutoSchema(tags=['User profiles'])
    serializer_class = MyTokenObtainPairSerializer