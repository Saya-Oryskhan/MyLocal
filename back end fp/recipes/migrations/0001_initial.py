# Generated by Django 4.1.7 on 2023-05-13 17:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cooking', models.IntegerField()),
                ('crop', models.IntegerField()),
                ('instruction', models.TextField(max_length=500)),
                ('rating', models.IntegerField(default=1)),
                ('calories', models.IntegerField()),
                ('total', models.IntegerField()),
                ('image', models.ImageField(blank=True, upload_to='photo/')),
                ('level', models.CharField(choices=[('EASY', 'Easy'), ('MEDIUM', 'Medium'), ('HARD', 'Hard')], max_length=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.category')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=150)),
                ('rating', models.IntegerField(default=1)),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text='The date and time the review was created.')),
                ('date_edited', models.DateTimeField(help_text='The date and time the review was last edited.', null=True)),
                ('image', models.ImageField(upload_to='')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.recipes')),
            ],
        ),
    ]
