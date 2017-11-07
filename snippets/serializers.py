from rest_framework import serializers
from snippets.models import User, Company, ROLES, MAN
from phonenumber_field.modelfields import PhoneNumberField


class UserSerializer(serializers.Serializer):
    
    username = serializers.CharField(required=True,max_length = 20)
    password = serializers.CharField(required=True,max_length = 16)
    list_of_roles = serializers.ChoiceField(choices=ROLES,default = 'MANAGER')

    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.list_of_roles = validated_data.get('list_of_roles', instance.list_of_roles)
        instance.save()
        return instance
    
    class Meta:
            model = User
            fields = ('username', 'password', 'list_of_roles')


class CompanySerializer(serializers.Serializer):
    name = serializers.CharField(required=True,max_length=30)
    tel = PhoneNumberField()
    email = serializers.EmailField(max_length=20)

    def create(self, validated_data):
        return Company.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.tel = validated_data.get('tel', instance.tel)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

    class Meta:
            model = Company
            fields = ('name', 'tel', 'email')