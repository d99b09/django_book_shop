from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer


class UserProfileSerializer(UserDetailsSerializer):
    uuid = serializers.UUIDField(source="profiles.uuid", read_only=True)

    class Meta(UserDetailsSerializer.Meta):
        fields = (
            'uuid',
            'username',
            'email',
            'first_name',
            'last_name',
            'address',
            'cart_number',
        )


    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profiles', {})
        print(profile_data)
        super(UserProfileSerializer, self).update(instance.user, validated_data)
        instance = update_userprofile(instance, validated_data, profile_data)
        return instance
