# Generated by Django 2.2.6 on 2020-05-11 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quiz',
            options={'verbose_name': 'Тест', 'verbose_name_plural': 'Тесты'},
        ),
        migrations.RemoveField(
            model_name='answer',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='multiple_correct_answers',
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('multiple_correct_answers', models.BooleanField(choices=[(True, 'Несколько правильных ответов'), (False, 'Один правильный ответ')], verbose_name='Количество верных ответов')),
                ('text', models.CharField(max_length=256, verbose_name='Текст вопроса')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Quiz', verbose_name='Вопрос')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quiz.Question', verbose_name='Тест'),
            preserve_default=False,
        ),
    ]
