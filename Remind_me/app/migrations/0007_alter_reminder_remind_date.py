# Generated by Django 4.2.3 on 2024-03-10 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_reminder_email_reminder_remind_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='remind_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
