# Generated by Django 5.0 on 2023-12-13 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.CharField(default='Some Description Here', max_length=60),
        ),
    ]