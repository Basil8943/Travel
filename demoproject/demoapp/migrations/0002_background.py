# Generated by Django 3.2.11 on 2022-02-07 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='background',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('back', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
