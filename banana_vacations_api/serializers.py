from rest_framework import serializers

from banana_vacations_api import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta: 
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style':{'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if  'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class PlannerNotesSerializer(serializers.ModelSerializer):
    """Serializes a note for the planner"""

    class Meta:
        model = models.PlannerNote
        fields = ('id', 'notes_text')

    def create(self, validated_data):
        """Create and return new note"""
        note = models.PlannerNote.objects.create_note(
            notes_text = validated_data['notes_text']
        )

        return note 


class DiaryEntrySerializer(serializers.ModelSerializer):
    """Serializes a note for the diary"""

    class Meta:
        model = models.Diary
        fields = ('id', 'diary_entry')

    def create(self, validated_data):
        """Create and return new diary entry"""
        entry = models.Diary.objects.create_entry(
            diary_entry = validated_data['diary_entry']
        )

        return entry