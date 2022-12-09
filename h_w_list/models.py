import datetime
from tabnanny import verbose
from django.db import models

from django.utils import timezone

class H_W(models.Model):
     h_w_title = models.CharField('Предмет', max_length = 200)
     h_w_text = models.TextField('Текст')
     pub_date = models.DateTimeField('Число на которое задано:')

     def __str__(self):
           return self.h_w_title
     
     def was_published_recently(self):
           return self.pub_date < timezone.now()


     
     class Meta:
          verbose_name = 'Д/З'
          verbose_name_plural = 'Д/З'
         