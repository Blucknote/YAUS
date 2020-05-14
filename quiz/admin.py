from django.contrib import admin

from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from tabbed_admin import TabbedModelAdmin

from quiz.forms import QuestionForm
from quiz.models import Answer, Quiz, Question


class AnswerAdminInline(NestedStackedInline):
    model = Answer
    extra = 2


class QuestionAdminInline(NestedStackedInline):
    model = Question
    form = QuestionForm
    extra = 1
    inlines = (
        AnswerAdminInline,
    )


class QuizAdmin(TabbedModelAdmin, NestedModelAdmin):
    tab_content = (
        (None, {
            'fields': (
                'title',
            )
        }),
    )

    tab_answers = (
        QuestionAdminInline,
    )

    tabs = (
        ('Контент', tab_content),
        ('Ответы', tab_answers),
    )

    verbose_name = 'Тест'
    verbose_name_plural = 'Тесты'


admin.site.register(Quiz, QuizAdmin)