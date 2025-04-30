from django import forms


class AreaCollectionForm(forms.Form):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter name"}
        ),
    )
