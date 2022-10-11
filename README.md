# <center>👉FULLSTACK PROJECT👈</center>

# <center>👩 PERSONAL LIST APP 👨</center>

<hr>

# <center> 💻 BACKEND 💻 </center>

<hr>

# <center> 🚀 INITIAL SETUP </center>

```bash
# CREATING VIRTUAL ENVIRONMENT
# windows 👇
python -m venv env
# linux / Mac OS 👇
vitualenv env

# ACTIVATING ENVIRONMENT
# windows 👇
source env/Scripts/activate
# linux / Mac OS 👇
source env/bin/activate

# PACKAGE INSTALLATION
# if pip does not work try pip3 in linux/Mac OS
pip install djangorestframework
pip freeze > requirements.txt
django-admin startproject main .
# alternatively python -m pip install django
pip install python-decouple
django-admin --version
```

```bash
# 💨 If you already have a requirement.txt file, you can install the packages in the file
# 💨 by entering the following commands respectively in the terminal 👇
1-python -m venv env
2-source env/Scripts/activate
3-pip install -r requirements.txt 🚀
4-python.exe -m pip install --upgrade pip
5-python manage.py migrate
6-python manage.py createsuperuser
7-python manage.py runserver
```

## 🛑 Secure your project

## 🚩 .gitignore

✔ Add a ".gitignore" file at same level as env folder, and check that it includes ".env" and /env lines.

🔹 Do that before adding your files to staging area, else you will need extra work to unstage files to be able to ignore them.

🔹 [On this page](https://www.toptal.com/developers/gitignore) you can create "gitignore files" for your projects.

## 🚩 Python Decouple

💻 To use python decouple in this project, first install it 👇

```bash
pip install python-decouple
```

💻 Go to terminal to update "requirements.txt"  👇

```bash
pip freeze > requirements.txt
```

✔ Create a new file and name as ".env" at same level as env folder

✔ Copy your SECRET_KEY from settings.py into this .env file. Don't forget to remove quotation marks and blanks from SECRET_KEY

```python
SECRET_KEY=-)=b-%-w+0_^slb(exmy*mfiaj&wz6_fb4m&s=az-zs!#1^ui7j
```

✔ Go to "settings.py", make amendments below 👇

```python
from decouple import config

SECRET_KEY = config('SECRET_KEY')
```

## 💻 INSTALLING DJANGO REST

💻 Go to terminal 👇

```bash
python manage.py makemigrations
python manage.py migrate
pip install djangorestframework
```

✔ Go to "settings.py" and add 'rest_framework' app to INSTALLED_APPS

## 💻 PostgreSQL Setup

💻 To get Python working with Postgres, you will need to install the “psycopg2” module👇

```bash
pip install psycopg2
```

💻 Go to terminal to update requirements.txt  👇

```bash
pip freeze > requirements.txt
```

✔ Go to settings.py and add '' app to INSTALLED_APPS

## 💻 Install Swagger

🔹 Explain a [sample API reference documentation](https://shopify.dev/api)

🔹 Swagger is an open source project launched by a startup in 2010. The goal is to implement a framework that will allow developers to document and design APIs, while maintaining synchronization with the code.

🔹 Developing an API requires orderly and understandable documentation.

🔹 To document and design APIs with Django rest framework we will use drf-yasg which generate real Swagger/Open-API 2.0 specifications from a Django Rest Framework API.

📜 You can find the documentation [here](https://drf-yasg.readthedocs.io/en/stable/readme.html).

### 💻 Go to terminal for installation 👇

```bash
pip install drf-yasg
```

💻 Go to terminal to update requirements.txt  👇

```bash
pip freeze > requirements.txt
```

✔ Go to "settings.py" and add 'drf_yasg' app to INSTALLED_APPS

## ✔ Here is the updated "urls.py" file for swagger. In swagger documentation, those patterns are not up-to-date 👇

```python
from django.contrib import admin
from django.urls import path, include

#! Three modules for swagger:
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Personal List App API",
        default_version="v1",
        description="Personal List App API project provides personal info",
        terms_of_service="#",
        contact=openapi.Contact(
            email="bayramemrekalkan@gmail.com"),  #! Change e-mail on this line!
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path("admin/", admin.site.urls),
    # Url paths for swagger:
    path("swagger(<format>\.json|\.yaml)",
         schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0),
         name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc",
         cache_timeout=0), name="schemaredoc"),
]
```

## 💻 MIGRATE 👇

```bash
python manage.py migrate
```

## 🚀 RUNSERVER 👇

```bash
python manage.py runserver
```

## ✔ After running the server, go to [swagger page](http://127.0.0.1:8000/swagger/) and [redoc page](http://localhost:8000/redoc/) of your project!

# <center> ✏ This is the end of initial setup ✏ </center>

<hr>

# <center> 🚀 AUTHENTICATION </center>

<hr>

## 🚩 ADDING AN APP

💻 Go to terminal 👇

```bash
python manage.py startapp users
```

✔ Go to "settings.py" and add 'users' app to "INSTALLED_APPS"

## 💻 INSTALL [DJ-REST-AUTH](https://dj-rest-auth.readthedocs.io/en/latest/)

```bash
pip install dj-rest-auth
```

💻 Go to terminal to update "requirements.txt"  👇

```bash
pip freeze > requirements.txt
```

## 🚩 Add "dj_rest_auth" app to "INSTALLED_APPS" in your django "base.py" 👇

```python
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
```

## 🚩 Go to "main/urls.py" and add the path 👇

```python
path('users/', include('users.urls'))
```

## ✔ Create "urls.py" file under "users" App 👇

## 🚩 Go to "users/urls.py" and add 👇

```python
from django.urls import path, include

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
]
```

## 💻 Migrate your database

```bash
python manage.py migrate
```

## ✔ Create "serializers.py" file under "users" App and add 👇

```python
from rest_framework import serializers, validators
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from dj_rest_auth.serializers import TokenSerializer
from rest_framework.authtoken.models import Token


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )
    first_name = serializers.CharField(
        max_length=100,
        required=True
    )
    last_name = serializers.CharField(
        max_length=100,
        required=True
    )
    password = serializers.CharField(
        write_only=True,
        # required=True,
        validators=[validate_password],
        style={"input_type": "password"}
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={"input_type": "password"}
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "password2"
        )

    def create(self, validated_data):
        password = validated_data.pop("password")
        validated_data.pop("password2")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError(
                {"password": "Password didn't match...."}
            )
        return data

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "full_name",
            "is_staff", #! For the buttons to be active in the frontend
        )
    def get_full_name(self,obj):
        return f"{obj.first_name.title()} {obj.last_name.upper()}"

class CustomTokenSerializer(TokenSerializer):
    user = UserSerializer(read_only=True)

    class Meta(TokenSerializer.Meta):
        model = Token
        fields = ("key", "user")
```

## 🚩 Go to "views.py"

```python
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
```

## 🚩 Go to "urls.py" and add the path 👇

```python
path("auth/register/",RegisterView.as_view(),name="register"),
```

## 🚩 Go to "settings.py" and add 👇

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}
```

## 🚩 Create "signals.py" under "user" App and add 👇

```python
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=User)
def create_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
```

## 🚩 Go to "apps.py" and add this under UsersConfig() 👇

```python
def ready(self) -> None:
    import account.signals
```

## 🚩 Go to "views.py" and customize RegisterView()👇

```python
from rest_framework import generics, status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    #! When user register 👉 "username", "email","first_name","last_name" and "token" will be returned. 👇
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = serializer.data
        if Token.objects.filter(user=user).exists():
            token = Token.objects.get(user=user).key
            data["token"] = token
        else:
            data["token"] = "No token created for this user.... :))"
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)
```

## 🚩 Override TokenSerializer() 👇

```python
from dj_rest_auth.serializers import TokenSerializer

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "full_name",
            "is_staff", #! For the buttons to be active in the frontend
        )
    def get_full_name(self,obj):
        return f"{obj.first_name.title()} {obj.last_name.upper()}"


#! We need to override the TokenSerializer to return all user data in a single request.
class CustomTokenSerializer(TokenSerializer):
    user = UserSerializer(read_only=True)

    class Meta(TokenSerializer.Meta):
        model = Token
        fields = ("key", "user")
```

## 🚩 Go to "settings.py" and add 👇

```python
REST_AUTH_SERIALIZERS = {
    'TOKEN_SERIALIZER': 'users.serializers.CustomTokenSerializer',
}
```

<hr>

