# Generated by Django 4.2.7 on 2024-03-24 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizs', '0003_rename_category_quiz_catagory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='catagory',
            new_name='category',
        ),
    ]