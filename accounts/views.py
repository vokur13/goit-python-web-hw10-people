# from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         return redirect(to="quotes:home")
    #     return super(SignUpView, self).dispatch(request, *args, **kwargs)
    #
    # def get(self, request, *args, **kwargs):
    #     return render(request, self.template_name, {"form": self.form_class()})
    #
    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data["username"]
    #         messages.success(request, f"Your account successfully created: {username}")
    #         return redirect(to="login")
    #     return render(request, self.template_name, {"form": form})
