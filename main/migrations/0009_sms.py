# Generated by Django 5.0.3 on 2024-12-05 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_contact_kirish'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ismiz', models.CharField(max_length=100)),
                ('gmail_ismi', models.CharField(max_length=100)),
                ('ishi', models.CharField(max_length=100)),
                ('xabar', models.CharField(max_length=100)),
            ],
        ),
    ]
