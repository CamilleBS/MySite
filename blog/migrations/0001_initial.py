# Generated by Django 3.0.6 on 2020-05-11 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=200)),
                ('post_body', models.CharField(max_length=20000)),
                ('post_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
