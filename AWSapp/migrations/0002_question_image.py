# Generated by Django 3.1.2 on 2024-02-08 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AWSapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='questions_images/'),
        ),
    ]
