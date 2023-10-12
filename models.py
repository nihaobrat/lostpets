from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class Animal(models.Model):
    """
    Модель животных
    """
    name = models.CharField(verbose_name='Имя', max_length=255)
    type = models.CharField(verbose_name='Вид животных', max_length=255)
    color = models.CharField(verbose_name='Цвет', max_length=255)
    weight = models.FloatField(verbose_name='Вес', max_length=10)
    age = models.PositiveIntegerField(verbose_name='Возраст', max_length=3)
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Животное'
        verbose_name_plural = 'Животные'


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email обязателен')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Модель пользователей
    """
    email = models.EmailField(verbose_name='Email', unique=True)
    first_name = models.CharField(verbose_name='Имя', max_length=30)
    last_name = models.CharField(verbose_name='Фамилия', max_length=30)
    date_joined = models.DateTimeField(verbose_name='Дата регистрации', auto_now_add=True)
    is_active = models.BooleanField(verbose_name='Активный', default=True)
    is_staff = models.BooleanField(verbose_name='Администратор', default=False)
    is_superuser = models.BooleanField(verbose_name='Суперпользователь', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name