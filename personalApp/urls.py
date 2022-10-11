from django.urls import path
from .views import DepartmentPersonalView, DepartmentView

urlpatterns = [
    path('', DepartmentView.as_view()),
    path('department/<str:department>/', DepartmentPersonalView.as_view()),
]
