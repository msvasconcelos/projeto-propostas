from rest_framework import serializers
from .models import Proposal, ProposalField, ProposalResponse, ProposalResponseField
from django.shortcuts import get_object_or_404

class ProposalFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProposalField
        fields = ['id', 'name']
        
class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = ['id', 'title', 'created_at']

class ProposalResponseFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProposalResponseField
        fields = ['id', 'response_value', 'proposal_field', 'response_model']


class ProposalResponseSerializer(serializers.ModelSerializer):
    proposal_model = serializers.PrimaryKeyRelatedField(queryset=Proposal.objects.all(), write_only=True)
    proposal_model_id = serializers.DictField(child=serializers.CharField(), write_only=True)
    documents = serializers.CharField(required=False)

    class Meta:
        model = ProposalResponse
        fields = ['id', 'proposal_model', 'proposal_model_id', 'status', 'name', 'documents']  # Adicionado o campo "name"

    def create(self, validated_data):
        proposal_model = validated_data.pop('proposal_model')
        proposal_model_id = validated_data.pop('proposal_model_id')
        name = validated_data.pop('name')  # Obtém o valor do campo "name"

        # Verificar se todos os campos fornecidos existem em ProposalField e pertencem a proposal_model
        proposal_fields = ProposalField.objects.filter(id__in=proposal_model_id.keys(), proposal=proposal_model)
        if len(proposal_fields) != len(proposal_model_id):
            raise serializers.ValidationError("Todos os campos da proposta devem ser respondidos.")

        proposal_response = ProposalResponse.objects.create(proposal_model=proposal_model, name=name, **validated_data)

        for field in proposal_fields:
            response_value = proposal_model_id[str(field.id)]
            ProposalResponseField.objects.create(
                response_model=proposal_response,
                proposal_field=field,
                response_value=response_value
            )

        return proposal_response
