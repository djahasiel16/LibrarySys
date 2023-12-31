# Generated by Django 5.0 on 2023-12-17 06:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_alter_book_copies'),
        ('borrower', '0002_borrowedbook_date_borrowed'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrowedbook',
            name='book_image_url',
        ),
        migrations.RemoveField(
            model_name='borrowedbook',
            name='copies',
        ),
        migrations.RemoveField(
            model_name='borrowedbook',
            name='description',
        ),
        migrations.RemoveField(
            model_name='borrowedbook',
            name='title',
        ),
        migrations.AddField(
            model_name='borrowedbook',
            name='b_book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.book'),
        ),
        migrations.AlterField(
            model_name='borrowedbook',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
