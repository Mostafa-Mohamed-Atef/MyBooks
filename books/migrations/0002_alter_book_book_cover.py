# Generated by Django 4.2.13 on 2024-07-19 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_cover',
            field=models.CharField(default='https://bookstoreromanceday.org/wp-content/uploads/2020/08/book-cover-placeholder.png', max_length=500),
        ),
    ]