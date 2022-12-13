from django import forms

from football_news_app.core.form_mixins import DisabledFormMixin
from football_news_app.photos.models import Photo, PhotoLike


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('publication_date', 'user')


class PhotoCreateForm(PhotoBaseForm):

    def __init__(self, *args, **kwargs):
        super(PhotoCreateForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['location'].widget.attrs.update({'class': 'form-control'})
        self.fields['tagged_teams'].widget.attrs.update({'class': 'form-control'})


class PhotoEditForm(PhotoBaseForm):
    class Meta:
        model = Photo
        exclude = ('publication_date', 'photo', 'user')

    def __init__(self, *args, **kwargs):
        super(PhotoEditForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['location'].widget.attrs.update({'class': 'form-control'})
        self.fields['tagged_teams'].widget.attrs.update({'class': 'form-control'})


class PhotoDeleteForm(DisabledFormMixin, PhotoBaseForm):
    disabled_fields = '__all__'
    exclude = ('photo',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['location'].widget.attrs.update({'class': 'form-control'})
        self.fields['tagged_teams'].widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):
        if commit:
            self.instance.tagged_teams.clear()
            PhotoLike.objects.filter(photo_id=self.instance.id).delete()
            self.instance.delete()
        return self.instance
