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