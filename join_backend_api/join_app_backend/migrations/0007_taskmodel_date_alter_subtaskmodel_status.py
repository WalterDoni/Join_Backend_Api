# Generated by Django 5.0.2 on 2024-03-12 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join_app_backend', '0006_subtaskmodel_status_alter_taskmodel_assignedto'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='date',
            field=models.CharField(default='31.12.2024', max_length=30),
        ),
        migrations.AlterField(
            model_name='subtaskmodel',
            name='status',
            field=models.CharField(blank=True, default='checked', max_length=10),
        ),
    ]