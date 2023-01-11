from django.db import models
from django.conf import settings
from authapp.models import MyUser

user_model_name: str = settings.AUTH_USER_MODEL


class Project(models.Model):
    """Это проект, для которого записаны To Do заметки"""

    name_project = models.CharField(
        max_length=255,
        verbose_name='Название проекта'
    )
    # url_project = models.EmailField(unique=True, max_length=254, null=False, verbose_name="ссылка на проект")
    url_project = models.URLField(
        verbose_name='Ссылка на репозиторий',
        max_length=200,
        help_text='Сылка не репозиторий длинной до 200 символов',
        unique=True,
        null=True,
        blank=True,
    )
    users_work_project = models.ManyToManyField(user_model_name, verbose_name='пользователи работающие над проектом')

    def __str__(self):
        return f'{self.name_project}'

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class ToDo(models.Model):
    """Это заметка."""
    project_todo = models.ForeignKey(
        verbose_name='Проект',
        to='mainapp.Project',
        on_delete=models.CASCADE
    )
    text = models.TextField(
        verbose_name='Текст заметки'
    )
    date_creation = models.DateTimeField(
        verbose_name='Дата и время создания',
        auto_now_add=True,
        db_index=True

    )
    date_updated = models.DateTimeField(
        verbose_name='Дата и время создания',
        auto_now_add=True,
        db_index=True

    )
    # author_todo = models.OneToOneField(user_model_name, on_delete=models.CASCADE, verbose_name='пользователь создавший заметку')
    author_todo = models.ForeignKey(
        verbose_name='пользователь создавший заметку',
        to=user_model_name,
        on_delete=models.CASCADE,

    )
    is_active = models.BooleanField(default=False, verbose_name='Запись активна')

    # def __str__(self):
    #     edge = 30
    #     text_ = (self.text[0:edge]
    #              if len(self.text) < edge
    #              else f'{self.text[0:edge]}...')
    #     return text_

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
