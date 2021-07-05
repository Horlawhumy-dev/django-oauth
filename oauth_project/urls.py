
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html")),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
]
# CLIENT_SECRET = 'TW5TOdHq_rL8umHWfU65PwHa'

# CLIENT_ID = '956053980126-u7qe61qfemu5eqi4k1t5o12guq15au6g.apps.googleusercontent.com'
