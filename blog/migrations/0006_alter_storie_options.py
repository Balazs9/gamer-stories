# Generated by Django 3.2 on 2022-01-24 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rename_textbox_comment_your_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='storie',
            options={'ordering': ['-posted_date']},
        ),
    ]
