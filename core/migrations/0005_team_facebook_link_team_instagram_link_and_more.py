# Generated by Django 4.1.4 on 2023-04-13 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_username_comment_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='facebook_link',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='instagram_link',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='linkedin_link',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='twitter_link',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ImageField(upload_to='assets/comment'),
        ),
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.ImageField(upload_to='assets/team'),
        ),
    ]