# Generated by Django 4.0.5 on 2022-07-29 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message_wolof', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sentences_wolof',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentence', models.TextField()),
            ],
        ),
    ]