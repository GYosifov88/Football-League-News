from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView

from football_news_app.photos.forms import PhotoCreateForm, PhotoEditForm, PhotoDeleteForm
from football_news_app.photos.models import Photo, PhotoLike
from football_news_app.photos.utils import get_photo_url


class PhotoListView(ListView):
    model = Photo
    template_name = 'photos/gallery-massonry.html'

    default_paginate_by = 15

    def get_photos_page(self):
        return self.request.GET.get('page', 1)

    def get_paginate_by(self, queryset):
        return self.request.GET.get('page size', self.default_paginate_by)

    def get_paginated_photos(self):
        page = self.get_photos_page()
        photos = self.object_list.all()
        paginator = Paginator(photos, self.default_paginate_by)
        return paginator.get_page(page)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photos'] = self.get_paginated_photos()
        return context


def get_post_photo_form(request, form, success_url, template_path, pk=None):
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(success_url)
    context = {
        'form': form,
        'pk': pk,
    }
    return render(request, template_path, context)


@login_required
def add_photo(request):
    if request.method == 'GET':
        form = PhotoCreateForm
    else:
        form = PhotoCreateForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            form.save_m2m()
            return redirect('details photo', pk=photo.pk)

    context = {
        'form': form
    }

    return render(request, 'photos/photo-add.html', context)


def details_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    is_liked_by_user = photo.photolike_set.filter(user_id=request.user.id) \
        .exists()
    context = {
        'photo': photo,
        'is_liked': is_liked_by_user,
        'likes_count': photo.photolike_set.count(),
        'is_owner': request.user == photo.user,
    }

    return render(request, 'photos/photo-details.html', context)


def edit_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    return get_post_photo_form(
        request,
        PhotoEditForm(request.POST or None, instance=photo),
        success_url=reverse_lazy('show photos'),
        template_path='photos/photo-edit.html',
        pk=pk,
    )


def delete_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    return get_post_photo_form(
        request,
        PhotoDeleteForm(request.POST or None, instance=photo),
        success_url=reverse('show photos'),
        template_path='photos/photo-delete.html',
        pk=pk,
    )


@login_required
def like_photo(request, photo_id):
    user_liked_photos = PhotoLike.objects.filter(
        photo_id=photo_id,
        user_id=request.user.pk,
    )

    if user_liked_photos:
        user_liked_photos.delete()
    else:

        PhotoLike.objects.create(
            photo_id=photo_id,
            user_id=request.user.pk,
        )

    return redirect(get_photo_url(request, photo_id))
