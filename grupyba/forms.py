# -*- coding: utf-8 -*-

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nome")
    email = forms.CharField(label="E-mail", widget=forms.TextInput(attrs={'size':30}))
    
    issues = [('', '-- escolha um assunto --'), ('Sugestão/Opinião', 'Sugestão/Opinião'),
        ('Reclamação', 'Reclamação'), ('Funcionalidade', 'Funcionalidade'), ('Eventos', 'Eventos'),
        ('Comunidade', 'Comunidade'), ('Dúvidas', 'Dúvidas'), ('Como Participar', 'Como Participar'),
        ('Usabilidade', 'Usabilidade'), ('Erro de informação', 'Erro de informação')]
    issue = forms.ChoiceField(choices=issues, widget=forms.Select(), label="Assunto")
    message = forms.CharField(widget=forms.Textarea, label="Mensagem")
    
    def clean_name(self):
        
        the_name = self.cleaned_data['name']
        
        if not len(the_name):
            raise forms.ValidationError("Campo obrigatório")

        return the_name
    
    def clean_email(self):
    
        email = self.cleaned_data['email']
        
        import re
        if not re.match(r'^[a-zA-Z0-9][\w\.-]*[a-zA-Z0-9]@[a-zA-Z0-9][\w\.-]*[a-zA-Z0-9]\.[a-zA-Z][a-zA-Z\.]*[a-zA-Z]$', email):
            raise forms.ValidationError("Entre com um endereço de e-mail válido.")
        
        return email
        
    def clean_message(self):
        message = self.cleaned_data['message']
        
        if len(message) < 20:
            raise forms.ValidationError("A mensagem deve ter no mínimo 20 caracteres.")
            
        return message    
