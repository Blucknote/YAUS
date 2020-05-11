from django.db import models


class Quiz(models.Model):
    title = models.CharField(
        max_length=128,
        verbose_name='Название теста'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Question(models.Model):
    MULTIPLE_CORRECT_CHOICES = (
        (True, 'Несколько правильных ответов'),
        (False, 'Один правильный ответ')
    )
    multiple_correct_answers = models.BooleanField(
        choices=MULTIPLE_CORRECT_CHOICES,
        verbose_name='Количество верных ответов',
    )
    text = models.CharField(
        max_length=256,
        verbose_name='Текст вопроса'
    )
    order = models.IntegerField(
        default=1
    )
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        verbose_name='Вопрос'
    )

    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.CharField(
        max_length=128,
        verbose_name='Текст ответа',
    )
    correct = models.BooleanField(
        default=False
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        verbose_name='Тест'
    )

    def __str__(self):
        return self.text
