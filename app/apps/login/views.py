from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.views import View
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect


class LoginFormView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login/login.html'

    def get_success_url(self):
        return '/'


class LogoutAuthView(View):
    redirect_to = '/login'

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(self.redirect_to)
