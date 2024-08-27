from django.shortcuts import render, redirect
from .forms import UserProfileForm
from .models import UserProfile
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views.generic import FormView
from django.contrib.auth.views import LoginView
# Create your views here.


class Register(FormView):
    template_name = 'accounts/base.html'
    form_class = UserProfileForm
    success_url = '/login/'
    
    def form_valid(self, form):
        name = self.request.POST['name']
        email = self.request.POST['email']
        password = self.request.POST['password1']
        user = UserProfile.objects.create_user(name=name, email=email, password=password)
        html_message = render_to_string('accounts/send_email.html', {'id': user.pk})
        plain_message = strip_tags(html_message)
        from_email = 'From <from@example.com>'
        to = 'to@example.com'
        send_mail("Email confirmation", plain_message, from_email, [to], html_message=html_message)
        return super().form_valid(form)

def confirm_email(request, id):
    user = UserProfile.objects.get(pk=id)
    user.email_confirmed = True
    user.save()
    return redirect('accounts:login')


class UserLogin(LoginView):
    template_name = 'accounts/base.html'
    
