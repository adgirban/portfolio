# Generated by Django 4.1.5 on 2024-04-21 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='tags',
            field=models.ManyToManyField(null=True, to='base.tag'),
        ),
    ]