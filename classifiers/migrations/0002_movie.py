# Generated by Django 2.2 on 2020-10-28 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifiers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
            ],
        ),
    ]
