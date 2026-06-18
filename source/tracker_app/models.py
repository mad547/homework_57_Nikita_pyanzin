from django.db import models


class Type(models.Model):
   name = models.CharField(
       max_length=100,
       null=False,
       blank=False,
       verbose_name='Название'
   )

   def __str__(self):
       return self.name

   class Meta:
       db_table = 'type'
       verbose_name = 'Тип'
       verbose_name_plural = 'Типы'


class Status(models.Model):
   name = models.CharField(
       max_length=100,
       null=False,
       blank=False,
       verbose_name='Название'
   )

   def __str__(self):
       return self.name

   class Meta:
       db_table = 'status'
       verbose_name = 'Статус'
       verbose_name_plural = 'Статусы'


class Project(models.Model):
    name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name='Название'
    )

    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Описание'
    )

    start_date = models.DateField(
        null=False,
        verbose_name='Дата начала'
    )

    end_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата окончания'
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'project'
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Issue(models.Model):
   summary = models.CharField(
       max_length=200,
       null=False,
       blank=False,
       verbose_name='Краткое описание'
   )

   description = models.TextField(
       null=True,
       blank=True,
       verbose_name='Полное описание'
   )

   status = models.ForeignKey(
       Status,
       on_delete=models.PROTECT,
       null=False,
       verbose_name='Статус'
   )

   issue_type = models.ManyToManyField(
       Type,
       related_name='issues',
       blank=True,
       verbose_name='Тип'
   )

   project = models.ForeignKey(
       Project,
       on_delete=models.CASCADE,
       null=True,
       blank=True,
       verbose_name='Проект'
   )

   created_at = models.DateTimeField(
       auto_now_add=True,
       verbose_name='Время создания'
   )

   updated_at = models.DateTimeField(
       auto_now=True,
       verbose_name='Время обновления'
   )

   def __str__(self):
       return self.summary

   class Meta:
       db_table = 'issue'
       verbose_name = 'Задача'
       verbose_name_plural = 'Задачи'
       ordering = ['-created_at']