# Generated by Django 4.1.6 on 2023-02-10 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_App', '0006_alter_myexperiences_css_class_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myprojects',
            name='features',
        ),
        migrations.AddField(
            model_name='myprojects',
            name='features1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='myprojects',
            name='features2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='myprojects',
            name='features3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='myprojects',
            name='features4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='myprojects',
            name='features5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='myprojects',
            name='tech_used',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
