from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class CreationForm(UserCreationForm):
    '''
    Форма регистрации нового пользователя.
    '''

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')
