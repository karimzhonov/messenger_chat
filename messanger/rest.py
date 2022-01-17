from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import BooleanField
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .models import Profile, User


class ProfileRest(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class UserRest(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class FriendsRestView(ListAPIView):
    serializer_class = ProfileRest

    def get_queryset(self):
        number = self.kwargs['number']
        return Profile.objects.get(pk=number).friends


class ProfileRestView(ListAPIView):
    serializer_class = ProfileRest

    def get_queryset(self):
        text = self.kwargs['text']
        qset = Profile.objects.filter(
            Q(first_name__icontains=text) |
            Q(last_name__icontains=text) |
            Q(user__username__icontains=text)
        )
        return qset


class UserRestView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserRest
    queryset = User.objects.all()


class AllProfilesRestView(ListAPIView):
    serializer_class = ProfileRest
    queryset = Profile.objects.all()
