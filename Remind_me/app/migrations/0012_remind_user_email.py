# Generated by Django 4.2.3 on 2024-03-11 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_remind_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='remind_user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
