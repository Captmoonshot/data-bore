# Generated by Django 2.2 on 2020-11-18 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classifiers', '0009_auto_20201030_0604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentiment',
            name='age',
            field=models.IntegerField(default=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sentiment',
            name='country',
            field=models.CharField(choices=[('United States of America', 'United States of America'), ('Canada', 'Canada'), ('Mexico', 'Mexico'), ('Europe', 'Europe'), ('Japan', 'Japan'), ('South Korea', 'South Korea')], default='Mexico', max_length=24),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sentiment',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sentiment',
            name='movie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='classifiers.Movie'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sentiment',
            name='results',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sentiment',
            name='reviews',
            field=models.TextField(default='Sux'),
            preserve_default=False,
        ),
    ]
