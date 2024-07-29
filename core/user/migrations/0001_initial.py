# Generated by Django 4.0.1 on 2024-07-29 14:01

import core.user.models
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core_comment', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core_post', '0002_rename_editable_post_edited'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('public_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(db_index=True, max_length=255, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('bio', models.TextField(null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=core.user.models.user_directory_path)),
                ('comments_liked', models.ManyToManyField(related_name='commented_by', to='core_comment.Comment')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('posts_liked', models.ManyToManyField(related_name='liked_by', to='core_post.Post')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
