# Generated by Django 4.0.4 on 2022-04-24 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='resource',
            field=models.FileField(upload_to='files/resources'),
        ),
    ]
