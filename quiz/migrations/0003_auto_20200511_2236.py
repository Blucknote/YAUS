# Generated by Django 2.2.6 on 2020-05-11 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20200511_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.CharField(max_length=128, verbose_name='Текст ответа'),
        ),
    ]
