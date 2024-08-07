from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email and password:
            raise ValueError('Введіть e-mail та пароль')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('is_staff must be True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('is_superuser must be True')
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    objects = CustomUserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


# class FriendsList(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='friend_list')
#     anime = models.ManyToManyField(CustomUser, blank=True)
#
#
# class WatchList(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='watch_list')
#     anime = models.ManyToManyField("anime.Anime", blank=True)
#
#
# class PlansList(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='plans_list')
#     anime = models.ManyToManyField("anime.Anime", blank=True)
#
#
# class AbandonedList(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='abandoned_list')
#     anime = models.ManyToManyField("anime.Anime", blank=True)
#
#
# class FavoriteList(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='favourite_list')
#     anime = models.ManyToManyField("anime.Anime", blank=True)
