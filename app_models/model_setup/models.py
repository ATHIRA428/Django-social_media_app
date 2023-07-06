from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # date_of_birth = models.DateField(null=True)
    GENDER_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Others')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    bio = models.TextField()
    website = models.URLField(blank=True)
    location = models.CharField(max_length=450)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.TextField()
    image_or_video_content = models.FileField(upload_to='post_content')
    publication_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, through='Like', related_name='liked_posts')
    count = models.IntegerField(default=0)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('user', 'post')

    # @classmethod
    # def toggle_like(cls, user, post):
    #     try:
    #         like = cls.objects.get(user=user, post=post)
    #         like.delete()  
    #         return False  
    #     except cls.DoesNotExist:
    #         cls.objects.create(user=user, post=post)
    #         return True  

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300, unique=True)
    posts = models.ManyToManyField(Post, related_name='tags')

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
