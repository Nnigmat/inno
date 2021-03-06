from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import UserProfile, USER_PROFILE_DATA


USER_STATUSES = [
    [1, "student"],
    [2, "faculty"],
    [3, "librarian"],
]


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=False)
    address = forms.CharField(required=False)
    phone_number = forms.IntegerField(required=True)
    photo = forms.FileField(required=False)
    status = forms.ChoiceField(choices=USER_STATUSES, required=True)

    class Meta:
        fields = [
            'username', 'first_name', 'last_name', 'email',  *USER_PROFILE_DATA
        ]
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        address = self.cleaned_data['address']
        phone_number = self.cleaned_data['phone_number']
        photo = self.cleaned_data['photo']
        status = dict(USER_STATUSES)[int(self.cleaned_data['status'])]
        if status == "librarian":
            user.is_staff = True
        if commit:
            user.save(True)
            UserProfile.objects.create(user=user, address=address, phone_number=phone_number, photo=photo, status=status)
            if status == "librarian":
                user.is_staff = True
                lib_group = Group.objects.get(name='Librarian')
                lib_group.user_set.add(user)
                lib_group.save()


class EditPatronForm(UserChangeForm):
    address = forms.CharField(required=False)
    phone_number = forms.IntegerField(required=False)
    photo = forms.CharField(required=False)
    status = forms.ChoiceField(choices=USER_STATUSES, required=True)

    class Meta(CreateUserForm.Meta):
        fields = [
            'username', 'first_name', 'last_name', 'email', 'password', *USER_PROFILE_DATA
        ]
