# Generated by Django 3.0.7 on 2020-06-19 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_auto_20200619_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default='default.jpeg', upload_to='profiles'),
        ),
    ]
