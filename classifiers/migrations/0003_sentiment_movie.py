# Generated by Django 2.2 on 2020-10-28 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classifiers', '0002_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentiment',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='classifiers.Movie'),
        ),
    ]
