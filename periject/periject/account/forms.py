from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username','first_name','last_name','email','password1','password2')
        model = get_user_model()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['first_name'].label = 'Firstname'
        self.fields['last_name'].label = 'Lastname'
        self.fields['email'].label = 'Email Adress'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Comfirm Password'