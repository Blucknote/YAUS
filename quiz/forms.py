from django.forms import ModelForm
from django.core.exceptions import ValidationError

from quiz.models import Question


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

    def clean(self):
        remaining_answers = [
            *filter(
                lambda answer: answer.get('DELETE', True) is False,
                self.nested_formsets[0].cleaned_data
            )
        ]
        if all(
            [
                *map(
                    lambda answer: answer.get('correct', False),
                    remaining_answers
                )
            ]
        ):
            raise ValidationError('Все ответы не могут быть правильными')
        if not any(
            [
                *map(
                    lambda answer: answer.get('correct', False),
                    remaining_answers
                )
            ]
        ):
            raise ValidationError('Минимум один правильный ответ')
        return self.cleaned_data
