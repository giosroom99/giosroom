# Generated by Django 4.1.6 on 2023-02-10 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_App', '0002_remove_myexperiences_experience_descriptions_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='myexperiences',
            name='css_class',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='myexperiences',
            name='css_id',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
