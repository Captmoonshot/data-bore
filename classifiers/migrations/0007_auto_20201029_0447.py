# Generated by Django 2.2 on 2020-10-29 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifiers', '0006_auto_20201029_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentiment',
            name='country',
            field=models.CharField(blank=True, choices=[('United States of America', 'United States of America'), ('Canada', 'Canada'), ('Mexico', 'Mexico'), ('Europe', 'Europe'), ('Japan', 'Japan'), ('South Korea', 'South Korea')], max_length=24, null=True),
        ),
    ]
