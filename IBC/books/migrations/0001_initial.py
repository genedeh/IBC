# Generated by Django 4.0 on 2021-12-22 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('name', models.CharField(max_length=20, unique=True)),
                ('slug', models.SlugField(primary_key=True, serialize=False, unique=True)),
                ('stars', models.SmallIntegerField()),
                ('story', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('description', models.TextField(help_text='Max text length is 200', max_length=200)),
                ('books', models.ManyToManyField(to='books.Book')),
            ],
        ),
    ]
