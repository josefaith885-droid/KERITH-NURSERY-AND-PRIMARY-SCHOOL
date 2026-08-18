from django.urls import include, path
from . import views  # Import views from your current app folder

# Optional but recommended: helps with URL namespacing
app_name = 'Core' 

urlpatterns = [
    # Example: maps the root of this app to a view named 'home'
    path('Core/', include('Core.urls')),
    ]
