# Generated by Django 4.1.3 on 2022-12-05 07:43

from django.db import migrations, models
import football_news_app.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_appuser_tickets'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile_photos/', validators=[football_news_app.core.validators.validate_file_less_than_7mb]),
        ),
    ]