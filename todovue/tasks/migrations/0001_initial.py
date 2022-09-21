# Generated by Django 4.1.1 on 2022-09-21 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=128)),
                ('done', models.BooleanField(default=True)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('doTo', models.TextField(blank=True, null=True)),
                ('projeto', models.TextField(blank=True, null=True)),
            ],
        ),
    ]