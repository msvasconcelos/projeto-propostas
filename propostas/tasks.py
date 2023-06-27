from __future__ import absolute_import, unicode_literals
from celery import shared_task
import requests
from propostas.models import Proposal

@shared_task
def process_proposal(proposal_id):
    proposal = Proposal.objects.get(id=proposal_id)

    # Prepare the data to be sent to the credit analysis API
    data = {
        # Populate with the necessary fields from the Proposal model
        'field1': proposal.field1,
        'field2': proposal.field2,
        # Add more fields as needed
    }

    # Make a request to the credit analysis API
    response = requests.post('https://loan-processor.digitalsys.com.br/analyze/', json=data)

    if response.status_code == 200:
        result = response.json()
        if result['approved']:
            # Proposal approved, update the status
            proposal.status = 'Approved'
        else:
            # Proposal denied, update the status
            proposal.status = 'Denied'

        # Save the updated proposal
        proposal.save()
