# Generated by Django 4.1.5 on 2024-04-21 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_work_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='thumbnail',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='images/'),
        ),
    ]
