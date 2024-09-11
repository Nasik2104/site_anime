from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models


class ListManager(models.Manager):
    def get_anime_list(self, anime, user):
        """
        This function returns the name of the list where the anime currently.
        Parameters:
            anime (Anime): The anime instance.
            user (CustomUser): The user instance.
        Returns:
            str: The name of the list where the anime is found.
        """

        list_mapping = {
            'favourite': FavoriteList,
            'watch': WatchList,
            'plans': PlansList,
            'abandoned': AbandonedList,
            'watched': WatchedList
        }

        for list_name, model in list_mapping.items():
            list_instance = model.objects.filter(user=user, anime=anime).first()
            if list_instance:
                return list_name

        return None

    def add(self, list_name, anime, user):
        """
        This function adds anime to the specified list.
        Parameters:
            list_name (str): The name of the list ('favourite', 'watch', etc.)
            anime (Anime): The anime instance to add.
            user (CustomUser): The user instance.
        """
        # Define the list models
        list_mapping = {
            'favourite': FavoriteList,
            'watch': WatchList,
            'plans': PlansList,
            'abandoned': AbandonedList,
            'watched': WatchedList
        }

        list_model = list_mapping.get(list_name)
        if list_model:
            for model in list_mapping.values():
                list_instance = model.objects.filter(user=user).first()
                if list_instance:
                    list_instance.anime.remove(anime)

            list_instance, _ = list_model.objects.get_or_create(user=user)
            list_instance.anime.add(anime)
        else:
            for model in list_mapping.values():
                list_instance = model.objects.filter(user=user).first()
                if list_instance:
                    list_instance.anime.remove(anime)


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


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='user_pictures', null=True, blank=True)
    nickname = models.CharField(max_length=64, null=True, blank=True)


class FriendsList(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='friend_list')
    friends = models.ManyToManyField(CustomUser, blank=True)


class BaseList(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='%(class)s')
    anime = models.ManyToManyField("anime.Anime", blank=True)

    objects = ListManager()

    class Meta:
        abstract = True


class WatchedList(BaseList):
    class Meta:
        verbose_name = 'Latched Lists'
        verbose_name_plural = 'Watched Lists'


class WatchList(BaseList):
    class Meta:
        verbose_name = "Watch List"
        verbose_name_plural = "Watch Lists"


class PlansList(BaseList):
    class Meta:
        verbose_name = "Plans List"
        verbose_name_plural = "Plans Lists"


class AbandonedList(BaseList):
    class Meta:
        verbose_name = "Abandoned List"
        verbose_name_plural = "Abandoned Lists"


class FavoriteList(BaseList):
    class Meta:
        verbose_name = "Favorite List"
        verbose_name_plural = "Favorite Lists"
