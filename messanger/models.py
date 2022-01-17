from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    # birth_date = models.DateField(blank=True)
    last_active_moment = models.DateTimeField(auto_now=True)
    created_moment = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    bio = models.TextField(blank=True)
    friends = models.ManyToManyField('Profile')

    def is_friends(self, profile):
        return profile.id in self.friends

    def get_full_name(self):
        if self.first_name or self.last_name:
            return f'{self.first_name} {self.last_name}'
        else:
            return self.user.username

    def __str__(self):
        return self.get_full_name()

    class Meta:
        ordering = ['-created_moment']


class GlobalMessage(models.Model):
    from_user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField()
    date_time = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='images/', blank=True)
    file = models.FileField(upload_to='files/', blank=True)

    def __str__(self):
        return f'From: {self.from_user.get_full_name()}||Message: {self.text}'

    class Meta:
        ordering = ['-date_time']


class ChatMessage(models.Model):
    text = models.TextField()
    date_time = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='images/', blank=True)
    file = models.FileField(upload_to='files/', blank=True)

    class Meta:
        ordering = ['-date_time']


class Chat(models.Model):
    members = models.ManyToManyField(Profile)
    messages = models.ManyToManyField(ChatMessage, blank=True)

    def __str__(self):
        return f'{self.members[0]} | {self.members[1]}'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


