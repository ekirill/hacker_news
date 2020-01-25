# Generated by Django 3.0.2 on 2020-01-25 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=1024, verbose_name='Title')),
                ('url', models.URLField(db_index=True, max_length=512, verbose_name='Link')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
