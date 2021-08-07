import re
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import UserForm


# To validate Phone Number
def validate(val):
    if re.match("^[6-9]\d{9}$", val):
        return val
    else:
        raise ValidationError("Enter a valid number")


class UserSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(source="mobile_Number", validators=[validate])

    class Meta:
        model = UserForm
        fields = ['id', 'name', 'date', 'email', 'phone_number']
