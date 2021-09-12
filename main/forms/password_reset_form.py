from django import forms

#form
class PasswordResetForm(forms.Form):
    '''
    reset password, email form
    '''

    username =  forms.EmailField(label='Email address (lower case)',
                                 widget=forms.TextInput(attrs={}) )      
