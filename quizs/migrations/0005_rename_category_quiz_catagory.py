# Generated by Django 4.2.7 on 2024-03-24 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizs', '0004_rename_catagory_quiz_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='category',
            new_name='catagory',
        ),
    ]
