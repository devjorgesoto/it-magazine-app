# Generated by Django 4.2 on 2023-05-04 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('headline', models.TextField(max_length=60)),
                ('description', models.TextField(max_length=160)),
                ('body', models.TextField(max_length=4000)),
                ('date_published', models.DateField(auto_now=True)),
                ('location', models.CharField(blank=True, max_length=30, null=True)),
                ('cover_image', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('short_description', models.TextField(blank=True, max_length=160)),
                ('long_description', models.TextField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date_published', models.DateField(auto_now=True)),
                ('body', models.TextField(max_length=4000)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.user')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.user'),
        ),
    ]
