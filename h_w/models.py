from django.db import models

class H_W_Send(models.Model):
     h_w_send_lesson = models.CharField('Предмет', max_length = 100)
     h_w_send_name = models.CharField('ФИО', max_length = 100)
     h_w_send_text = models.TextField('Текст задания')
     

     def __str__(self):
           return self.h_w_send_name
     
     


     
     class Meta:
          verbose_name = 'Отправленное Д/З'
          verbose_name_plural = 'Отправленные Д/З'


class H_W_Image_Send(models.Model):
     h_w_send_image_lesson = models.CharField('Предмет', max_length = 100)
     h_w_send_image_name = models.CharField('ФИО', max_length = 100)
     h_w_send_image_text = models.CharField('Текст задания', max_length = 100)
     h_w_send_image = models.ImageField('Фото задания', upload_to='images/')

     

     def __str__(self):
           return self.h_w_send_image_name
     
     


     
     class Meta:
          verbose_name = 'Отправленное Д/З в виде фото'
          verbose_name_plural = 'Отправленные Д/З в виде фото'






