# Generated by Django 4.2.4 on 2023-09-05 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='description',
            field=models.TextField(null=True),
        ),
    ]