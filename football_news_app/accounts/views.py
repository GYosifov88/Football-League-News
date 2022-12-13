from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import DetailView, UpdateView, DeleteView

from football_news_app.accounts.forms import UserCreateForm


UserModel = get_user_model()


class SignInView(LoginView):
    template_name = 'accounts/user-sign-in.html'


class SignUpView(views.CreateView):
    template_name = 'accounts/user-sing-up.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)

        return result


class SignOutView(LogoutView):

    next_page = reverse_lazy('index')


class UserDetailsView(DetailView):
    template_name = 'accounts/user-profile.html'
    model = UserModel
    photos_paginate_by = 3

    def get_photos_page(self):
        return self.request.GET.get('page', 1)

    def get_paginated_photos(self):
        page = self.get_photos_page()
        photos = self.object.photo_set.order_by('-publication_date')
        paginator = Paginator(photos, self.photos_paginate_by)
        return paginator.get_page(page)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.request.user == self.object
        context['is_owner'] = self.request.user == self.object
        photos = self.object.photo_set.all() \
            .prefetch_related('photolike_set')
        context['photos_count'] = photos.count()
        context['likes_count'] = sum(x.photolike_set.count() for x in photos)
        context['photos'] = self.get_paginated_photos()

        return context


class UserEditView(LoginRequiredMixin, UpdateView):
    template_name = 'accounts/user-edit.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'email', 'profile_photo',)

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk
        })


class UserDeleteView(DeleteView):
    template_name = 'accounts/user-delete.html'
    model = UserModel
    success_url = reverse_lazy('index')

