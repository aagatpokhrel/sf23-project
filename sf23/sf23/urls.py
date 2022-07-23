
from django.contrib import admin
from django.urls import path, include
from ExpenseTracker import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("ExpenseTracker.urls"))
]
