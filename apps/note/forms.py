from django import forms
from tinymce.widgets import TinyMCE
from .models import Note
    
    
class NoteForm(forms.ModelForm):    
    comment = forms.CharField(widget=TinyMCE(attrs={'cols': 30, 'rows': 10}))
   
    class Meta:       
        model = Note        
        fields = ('transaction', 'comment', 'edited_by')


class NoteUpdateForm(forms.ModelForm):    
    comment = forms.CharField(widget=TinyMCE(attrs={'cols': 30, 'rows': 10}))
   
    class Meta:       
        model = Note        
        fields = ('comment', 'edited_by')


class NoteAddForm(forms.ModelForm):    
    comment = forms.CharField(widget=TinyMCE(attrs={'cols': 30, 'rows': 10}))
   
    class Meta:       
        model = Note        
        fields = ('transaction', 'comment', 'edited_by')