from django import forms
from .models import Driver, Car


class DriverLicenseUpdateForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ["license_number"]

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]
        if not (len(license_number) == 8 and
                license_number[:3].isupper() and
                license_number[:3].isalpha() and
                license_number[3:].isdigit()):
            raise forms.ValidationError(
                "License must be 8 characters long: 3 uppercase letters followed by 5 digits."
            )
        return license_number


    class CarForm(forms.ModelForm):
        class Meta:
            model = Car
            fields = "__all__"
            widgets = {
                "drivers": forms.CheckboxSelectMultiple()
            }
