from .models import H_W_Send, H_W_Image_Send
from django.forms import ModelForm, TextInput, Textarea,ImageField



class H_W_Send_Form(ModelForm):
    class Meta:
        model = H_W_Send
        fields = ["h_w_send_name", "h_w_send_lesson", "h_w_send_text"]
        widgets = {
            "h_w_send_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'

        }),
            "h_w_send_lesson": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите предмет'

        }),
            "h_w_send_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст'

        })
        }


class H_W_Image_SendForm(ModelForm):

    class Meta:
        model = H_W_Image_Send
        fields = '__all__'   
        widgets = {
            "h_w_send_image_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'

        }),
            "h_w_send_image_lesson": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите предмет'

        }),
            "h_w_send_image_text": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст'

        })
        }  
                


        
        