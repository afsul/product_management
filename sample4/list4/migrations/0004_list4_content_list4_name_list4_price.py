# Generated by Django 4.0.2 on 2022-02-19 05:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('list4', '0003_alter_list4_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='list4',
            name='content',
            field=models.CharField(default=django.utils.timezone.now, max_length=700),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='list4',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='list4',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
