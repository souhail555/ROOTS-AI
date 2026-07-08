from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Car, Project

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'role']

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            role=validated_data.get('role', 'participant')
        )


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ['owner']


class CarSerializer(serializers.ModelSerializer):
    def validate_project(self, project):
        request = self.context.get('request')
        if not request or not request.user.is_authenticated:
            return project

        user = request.user
        is_admin = user.is_superuser or user.is_staff or getattr(user, 'role', None) == 'admin'
        if is_admin:
            return project

        if project.owner_id != user.id:
            raise serializers.ValidationError('You can only add cars to your own projects.')
        return project

    class Meta:
        model = Car
        fields = '__all__'
        read_only_fields = ['owner']
