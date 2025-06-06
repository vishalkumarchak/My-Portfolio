# Generated by Django 5.1.6 on 2025-04-13 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('technologies', models.CharField(max_length=255)),
                ('github_link', models.URLField()),
                ('live_link', models.URLField(blank=True)),
                ('image', models.ImageField(upload_to='projects/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
