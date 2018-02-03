from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from.models import UserProfile


USER_STATUSES = [
    [1, "student"],
    [2, "faculty"],
    [3, "librarian"],
]


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    address = forms.CharField(required=True)
    phone_number = forms.IntegerField(required=True)
    status = forms.ChoiceField(choices=USER_STATUSES, required=True)

    class Meta:
        fields = [
            'username', 'first_name', 'last_name', 'email', 'address', 'phone_number', 'status'
        ]
        model = User


    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        address = self.cleaned_data['address']
        phone_number = self.cleaned_data['phone_number']
        status = dict(USER_STATUSES)[int(self.cleaned_data['status'])]
        if commit:
            user.save(True)
            UserProfile.objects.create(user=user, address=address, phone_number=phone_number, status=status)


class EditPatronForm(UserChangeForm):
    address = forms.CharField(required=True)
    phone_number = forms.IntegerField(required=True)

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'email', 'phone_number', 'address'
        ]

