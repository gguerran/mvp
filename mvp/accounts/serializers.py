from rest_framework import serializers

from mvp.accounts.models import Advertiser


class CreateAdvertiserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Advertiser
        fields = [
            'id', 'name', 'email', 'is_active', 'phone', 'created_at',
            'password1', 'password2'
        ]
        extra_kwargs = {
            'id': {'read_only': True}, 'created_at': {'read_only': True},
            'is_active': {'read_only': True}
        }
    
    def create(self, validated_data):
        password = validated_data.pop('password1')
        password2 = validated_data.pop('password2')
        if password == password2:
            user = Advertiser(**validated_data)
            user.set_password(password)
            user.save()
            return user
        raise serializers.ValidationError('As senhas não conferem')


class AdvertiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertiser
        fields = [
            'id', 'name', 'email', 'is_active', 'phone', 'created_at',
        ]
        extra_kwargs = {
            'id': {'read_only': True}, 'created_at': {'read_only': True},
            'is_active': {'read_only': True}
        }


class UpdatePassAdvertiserSerializer(serializers.ModelSerializer):
    last_pass = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = Advertiser
        fields = [
            'id', 'name', 'email', 'phone', 'is_active', 'last_pass',
            'password', 'password2', 'created_at',
        ]
        extra_kwargs = {
            'id': {'read_only': True}, 'name': {'read_only': True},
            'email': {'read_only': True}, 'phone': {'read_only': True},
            'is_active': {'read_only': True}, 'password': {'write_only': True},
        }

    def update(self, instance, validated_data):
        if instance.check_password(validated_data['last_pass']):
            if validated_data['password'] == validated_data['password2']:
                instance.set_password(validated_data['password'])
                instance.save()
                return instance
            raise serializers.ValidationError('As senhas não conferem')
        raise serializers.ValidationError('Antiga senha inválida')
