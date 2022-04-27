from django import forms
from .models import Login

class LoginForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    def __init__(self, *args, **kwargs):
        
        super(LoginForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            
            if field.widget.__class__ == forms.widgets.TextInput or field.widget.__class__ == forms.widgets.PasswordInput:
                print('name', name)
                if 'class' in field.widget.attrs:
                    field.widget.attrs['class'] += 'class-' + name
                else:
                    field.widget.attrs.update({'class':'class-' + name})
                if name == 'password':
                    print('AJAJA')
                    
                    field.widget.attrs.update({'placeholder':'********','data-toggle': 'password'})
                # #     field.widget.__class__ = forms.widgets.PasswordInput
                #if 'id_for_label' in field.widget.attrs:
                 #   field.widget.attrs['id_for_label'] += 'id_for_label-' + name
                
                #field.widget.attrs.update({'label':name.upper()})
    class Meta:
        model = Login
        fields = ('name', 'password')
        
        
        
