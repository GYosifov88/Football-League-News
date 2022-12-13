# Generated by Django 4.1.3 on 2022-11-14 11:00

from django.db import migrations, models
import django.db.models.deletion
import football_news_app.core.model_mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('personal_photo', models.URLField()),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('biography', models.TextField()),
                ('position', models.CharField(choices=[('goalkeeper', 'Goalkeeper'), ('defender', 'Defender'), ('midfielder', 'Midfielder'), ('attacker', 'Attacker')], max_length=10)),
                ('nationality', models.CharField(max_length=30)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='teams.team')),
            ],
            bases=(football_news_app.core.model_mixins.StrFromFieldsMixin, models.Model),
        ),
    ]
