from django import forms
#vowels='aeiouAEIOU'
def call_error(Svalue):
    if Svalue[0].lower=='a':
    #if Svalue[0] in vowels:
        raise forms.ValidationError('Date is not startted with a')
    
def len_error(name):
    if len(name)<=5:
        raise forms.ValidationError('len is lessthan 5')



class StudentForm(forms.Form):
    
    sname=forms.CharField(validators=[call_error,len_error])
    sage=forms.IntegerField()
    Email=forms.EmailField(validators=[call_error])