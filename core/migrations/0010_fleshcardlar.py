# Generated by Django 4.1.4 on 2023-04-15 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_asosiy_malumotlar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fleshcardlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
            ],
        ),
    ]
