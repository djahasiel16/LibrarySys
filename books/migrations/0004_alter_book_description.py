# Generated by Django 5.0 on 2023-12-13 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.CharField(default='Some Description Here', max_length=100),
        ),
    ]
