# Generated by Django 4.0.4 on 2022-10-31 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AyucareApp', '0004_purchased_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_name',
            new_name='username',
        ),
    ]