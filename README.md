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


## 🔑 PROJECT REQUEST 👇

- We will have Department and Personal tables and we will link them together. Each department will have its own personnel under it.

- At the end of the full stack project, the company personnel who log in will be able to see the company's departments and the personnel working under those departments in detail.

- Staff members will be able to add new staff to the list and update them.

- Our Personal model will have the "is_staffed" option. If this option is true, we will query the User table according to the user's first and last name, and if there is a user, we will set the is_staff property to true from the information in the User table of that staff.

- Only superusers will have the authority to delete staff.

- We will make this structure using "generic view". In order to override Class methods, we will provide if-else structures that should act accordingly whether the person is a staff or superuser. We will use IsAuthenticated from Rest framework permissions.

- We will use nested serializer and methodfields in our serializer.

- We will use token authentication. We will delete the token when the user logs out.

- We will use the cors-headers package to connect the frontend to our API.

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

#! We generate a token for the user in signals.py so that the user can login when she registers, so that the user can log in directly when she registers.
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

## <center> END OF AUTHENTICATION </center>

<hr>

## 💻 Go to terminal and create "personalApp" app 👇

```bash
python manage.py startapp personalApp
```

✔ Go to "settings.py" and add 'personalApp' app to "INSTALLED_APPS"

## 🚩 Create the following files under "personalApp" app 👇

- urls.py

- serializers.py

- signals.py

## 🚩 Go to "models.py" and create models 👇

```python
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Personal(models.Model):
    #* "SET_NULL" makes the corresponding field "null" when the user is deleted
    #! When we use "set_null" we have to say "null=True" 👇

    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='departments')

    #? related_name="deparments" tells us that the staffs are related to the deparment and is used to call it later. We can check the relationship with "deparment.id" and "personnel.id".
    #* related_name="deparments" tells us that staffs are related to deparment and it is used to call later for convenience. We can check the relation with "deparment.id" and "personnel.id". 👆

    create_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_staffed = models.BooleanField(default=False)

    TITLE = (
        ("Team Lead", "LEAD"),
        ("Mid Lead", "MID"),
        ("Junior", "JUN"),
    )
    title = models.CharField(max_length=50, choices=TITLE)

    GENDER =(
        ("Female", "F"),
        ("Male", "M"),
        ("Other", "O"),
        ("Prefer Not Say", "N"),
    )
    gender = models.CharField(max_length=50, choices=GENDER)
    salary = models.IntegerField(default=1250)
    start_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} : {self.first_name} {self.last_name}"
```

## 🚩 Register the models in "admin.py" 👇

```python
from django.contrib import admin
from personalApp.models import Department, Personal

admin.site.register(Department)
admin.site.register(Personal)
```

## 💻 Migrate your database 👇

```bash
python manage.py makemigrations
python manage.py migrate
```

## 🚩 To create serializers go to "serializers.py" 👇

```python
from rest_framework import serializers
from .models import Department, Personal
from django.utils.timezone import now

class DepartmentSerializer(serializers.ModelSerializer):
    personal_count = serializers.SerializerMethodField()
    class Meta:
        model = Department
        fields = ('id', 'name', 'personal_count')

    def get_personal_count(self, obj):
        return Personal.objects.filter(department = obj.id).count() #! 👈 We counted the personnel in the departments.

class PersonalSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField()
    #* https://www.django-rest-framework.org/api-guide/fields/#serializermethodfield 👆

    create_user = serializers.StringRelatedField()
    #* https://www.django-rest-framework.org/api-guide/relations/#stringrelatedfield 👆

    class Meta:
        model = Personal
        fields = "__all__"

    def get_days_since_joined(self, obj):
        return (now() - obj.start_date).days #! 👈 converts the result to "days"

class DepartmentPersonalSerializer(serializers.ModelSerializer):
    personal_count = serializers.SerializerMethodField()
    #? "deparments" comes from the related name in the model 👇
    departments = PersonalSerializer(many=True, read_only=True)
    class Meta:
        model = Department
        fields = ('id', 'name', 'personal_count', 'departments')

    def get_personal_count(self, obj):
        return Personal.objects.filter(department = obj.id).count()
```

## 🚩 Go to "views.py" and start to create views 👇

```python
from django.shortcuts import render
from rest_framework import status
from rest_framework import generics
from personalApp.models import Department, Personal
from rest_framework.generics import GenericAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from personalApp.serializers import DepartmentPersonalSerializer, DepartmentSerializer, PersonalSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

class DepartmentView(generics.ListAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    permission_classes = [IsAuthenticated]
    #! only logged in users can make a get request 👆
```

## 🚩 Add the path in "urls.py" 👇

```python
from django.urls import path
from .views import DepartmentView

urlpatterns = [
    path('', DepartmentView.as_view()),
]
```

## 🚩 Go to "main/urls.py" and add the path 👇

```python
path('api/',include('personalApp.urls')),
```

## ✔ Add departments in admin panel and check if get method works in [Postman](https://www.postman.com/)

## 🚩 Create "DepartmentPersonelView()" in "views.py" 👇

```python
class DepartmentPersonalView(generics.ListAPIView):
    serializer_class = DepartmentPersonalSerializer
    queryset = Department.objects.all()
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        name = self.kwargs['department']
        return Department.objects.filter(name__iexact=name)
        #! We have made a dynamic url. The user will be able to send requests based on the department name and display only the relevant department.
        #?"name__iexact" method to ignore lowercase or uppercase. This method is used to filter.
```

## 🚩 Add the path in "urls.py" 👇

```python
path('department/<str:department>/', DepartmentPersonalView.as_view()),
```

## 🚩 Create PersonalListCreate() in view.py 👇

```python
class PersonalListCreate(ListCreateAPIView):
    queryset = Personal.objects.all()
    serializer_class=PersonalSerializer
    # permission_classes = [IsAuthenticated]
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if self.request.user.is_superuser or self.request.user.is_staff:
            #! If the related user is "staff" or "superuser", he/she can "create personnel" 👆
            self.perform_create(serializer)
            data = {
                "message": f"Personal {serializer.validated_data.get('first_name')} saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = {
                "message": "You are not authorized to perform this operation"
            }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)
    def perform_create(self, serializer):
        serializer.save()
```

## 🚩 Create "PersonalGetUpdateDelete() in views.py 👇

```python
class PersonalGetUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Personal.objects.all()
    serializer_class=PersonalSerializer
    # permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    #! Since the default lookup-field is "pk", when we send it from the url with pk, it happens even if we don't write it. 👆

    def put(self, request, *args, **kwargs):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return self.update(request, *args, **kwargs)
        else:
            data = {
                "message": "You are not authorized to perform this operation"
            }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if self.request.user.is_superuser:
            self.perform_destroy(instance)
            data = {
                "message": f"Name: {instance.first_name} deleted."
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)
        else:
            data = {
                "message": "You are not authorized to perform this operation"
            }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)

    def perform_destroy(self, instance):
        instance.delete()
```

## 🚩 Add the path in "urls.py" 👇

```python
path('personal/', PersonalListCreate.as_view()),
path('personal/<int:pk>/', PersonalGetUpdateDelete.as_view()),
```

## 🚩 Go to "signals.py" and add 👇

```python
from django.contrib.auth.models import User
from .models import Personal
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Personal)
def is_staffed_user(sender, instance, **kwargs):
    if instance.is_staffed:
        user = User.objects.get(first_name=instance.first_name, last_name=instance.last_name)
        if user:
            user.is_staff = True
            user.save()
        else:
            instance.is_staffed = False
            instance.save()
```

## 🚩 Go to "apps.py" and add 👇

```python
 def ready(self):
    import personalApp.signals
```

## <center>✨ END OF BACKEND 🎉</center>

<hr>

# <center>📢 FOR DJANGO DEPLOYMENT YOU CAN USE "PYTHON ANY WHERE"</center>

## 💻 Commands for setup 👇

```bash
    git clone https://github.com/githubUserName/projectName.git
    cd projectName
    python -m venv env
    source env/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    echo SECRET_KEY=write_random_chars_to_here > .env
    python manage.py migrate
    $ python manage.py createsuperuser # optional
```

## 💻 Command for learn to current path 👇

```bash
    pwd
```

- "Add New Web App" with ManualConfigration with Python_LastVersion

- Set "Source Code" with "Main Path" (example: /home/anyWhereUserName/ProjectName)

- Set "Working Directory" with "Main Path" (example: /home/anyWhereUserName/ProjectName)

- Set "VirtualEnv" with "Env Path" (example: /home/anyWhereUserName/ProjectName/env)

## 🚩 pythonanywhere/Web -> WSGI Configuration File(pythonanywhere_com_wsgi.py) 👇

```python
    import os
    import sys

    # Set: Project Main Path:
    path = '/home/anyWhereUserName/ProjectName'

    if path not in sys.path:
        sys.path.append(path)

    # Set: Where is settings.py:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'projectFolderName.settings'

    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
```

## 👍 Finished 😎

## ‼ Don't forget 👉 click to 'Reload' button before publish.

    if error, checking:

        settting.py:

            ALLOWED_HOSTS = ['*']

            # folder -> static-files-path:
            STATIC_URL = 'static/'
            # root -> static-files-path:
            STATIC_ROOT = BASE_DIR / STATIC_URL
            # Alternates:
            # if in base folder -> STATIC_ROOT = BASE_DIR / 'static/'
            # if in app folder -> STATIC_ROOT = BASE_DIR / 'appFolderName/static/'

        urls.py:

            from django.conf import settings
            from django.conf.urls.static import static
            # url -> static-files-path:
            urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

<hr>

<center><img align="center"
  src="https://www.freecodecamp.org/news/content/images/2021/06/Ekran-Resmi-2019-11-18-18.08.13.png"  width="90px"></center>

# <center> FOR REACT CONFIGURATION <center>

# <center>✔ DJANGO-CORS-HEADERS ✔</center>

<hr>


<hr>

🔑 A Django App that adds [Cross-Origin Resource Sharing (CORS)](https://github.com/adamchainz/django-cors-headers) headers to responses.

🔑 This allows in-browser requests to your Django application from other origins.

🔑 Adding CORS headers allows your resources to be accessed on other domains.

🔑 It's important you understand the implications before adding the headers, since you could be unintentionally opening up your site's private data to others.

## 💻 To install cors 👇

```bash
pip install django-cors-headers
```

## ✔ Add 'corsheaders' to "INSTALLED_APPS" in "settings.py"

## 🚩 You will also need to add a middleware class to listen in on responses 👇

```python
MIDDLEWARE = [
    ...,
    "corsheaders.middleware.CorsMiddleware",
    ...,
]
```

## 🚩 To allow all origins add 👇

```python
CORS_ALLOW_ALL_ORIGINS=True
```

## 🚩 Add a list of HTTP verbs that are allowed for the actual request 👇

```python
CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]
```

## 💻 Runserver 👇

```bash
python manage.py runserver
```

## 💻 Open the React Project and start it 👇

```bash
yarn start
```

<hr>