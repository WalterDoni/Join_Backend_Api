# Generated by Django 5.0.2 on 2024-02-27 12:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Max Mustermann', max_length=100)),
                ('email', models.CharField(default='Max@Musteremail.at', max_length=100)),
                ('phonenumber', models.CharField(default='0123456', max_length=100)),
                ('short', models.CharField(default='MM', max_length=5)),
                ('iconColor', models.CharField(default='#FF7A00', max_length=20)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
