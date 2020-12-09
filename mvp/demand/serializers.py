from rest_framework import serializers

from mvp.demand.models import Demand


class DemandSerializer(serializers.ModelSerializer):

    class Meta:
        ordering = ['created_at']
        model = Demand
        fields = [
            'id', 'description', 'state', 'city', 'district', 'street',
            'number', 'email', 'phone', 'status', 'advertiser', 'created_at'
        ]
        extra_kwargs = {
            'advertiser': {'required': False}, 'id': {'read_only': True},
            'email': {'read_only': True}, 'phone': {'read_only': True},
            'created_at': {'read_only': True}
        }


class SetFinishedDemandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Demand
        ordering = ['created_at']
        fields = [
            'id', 'description', 'state', 'city', 'district', 'street',
            'number', 'email', 'phone', 'status', 'advertiser', 'created_at'
        ]
        extra_kwargs = {
            'id': {'read_only': True}, 'description': {'read_only': True},
            'state': {'read_only': True}, 'city': {'read_only': True},
            'district': {'read_only': True}, 'street': {'read_only': True},
            'number': {'read_only': True}, 'email': {'read_only': True},
            'phone': {'read_only': True}, 'advertiser': {'read_only': True},
            'created_at': {'read_only': True}
        }

    def update(self, instance, validated_data):
        if instance.status == 'Finalizada' and \
            validated_data['status'] == 'Aberta':
            raise serializers.ValidationError(
                'A demanda já estava finalizada, você não pode reabri-la.'
            )

        if instance.status == 'Finalizada' and \
            validated_data['status'] == 'Finalizada':
            raise serializers.ValidationError('A demanda já estava finalizada')

        if instance.status == 'Aberta' and \
            validated_data['status'] == 'Aberta':
            raise serializers.ValidationError('A demanda já estava aberta.')

        instance.status = validated_data['status']
        instance.save()
        return instance
