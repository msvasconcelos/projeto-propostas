from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import filters
from .models import Proposal, ProposalField, ProposalResponse, ProposalField
from .serializers import ProposalSerializer, ProposalFieldSerializer, ProposalResponseSerializer
from django.shortcuts import render
    
class ProposalViewSet(viewsets.ModelViewSet):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer
    lookup_field = 'id'

class ProposalFieldViewSet(viewsets.ModelViewSet):
    queryset = ProposalField.objects.all()
    serializer_class = ProposalFieldSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        proposal_id = self.request.query_params.get('proposal', None)
        if proposal_id is not None:
            proposal_id = int(proposal_id)
            queryset = queryset.filter(proposal_id=proposal_id)
        return queryset

class ProposalResponseViewSet(viewsets.ModelViewSet):
    queryset = ProposalResponse.objects.all()
    serializer_class = ProposalResponseSerializer
    lookup_field = 'id'

    def perform_create(self, serializer):
        proposal = Proposal.objects.get(pk=self.request.data['proposal_model'])
        serializer.save(proposal_model=proposal)
        
def proposal_details(request):
    proposal_id = request.GET.get('proposal_id')
    proposal_fields = ProposalField.objects.filter(proposal=proposal_id)

    context = {
        'proposal_fields': proposal_fields,
    }

    return render(request, 'proposal-details.html', context)