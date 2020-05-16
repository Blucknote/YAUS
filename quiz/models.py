from django.db import models
from django.utils.text import slugify


class Quiz(models.Model):
    title = models.CharField(
        max_length=128,
        verbose_name='Название теста'
    )
    description = models.TextField(
        max_length=512,
        verbose_name='Описание теста'
    )
    slug = models.SlugField(
        max_length=128,
        help_text='Fills by self'
    )

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Quiz, self).save()

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
        verbose_name='Вопрос',
        related_name='questions'
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
        verbose_name='Тест',
        related_name='answers'
    )

    def __str__(self):
        return self.text
