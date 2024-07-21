# Generated by Django 4.2.13 on 2024-07-18 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=225)),
                ('author_name', models.CharField(max_length=225)),
                ('book_genre', models.CharField(max_length=225)),
                ('book_year', models.IntegerField()),
                ('book_cover', models.CharField(max_length=500)),
                ('page_number', models.IntegerField()),
                ('finished_date', models.DateField()),
            ],
        ),
    ]