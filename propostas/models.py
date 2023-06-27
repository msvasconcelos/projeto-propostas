from django.db import models

class Proposal(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Proposal #{self.pk}"


class ProposalField(models.Model):
    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProposalResponse(models.Model):
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Aprovado', 'Aprovado'),
        ('Reprovado', 'Reprovado'),
    ]

    proposal_model = models.ForeignKey(Proposal, on_delete=models.CASCADE, related_name='responses')
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Pendente')
    fields = models.ManyToManyField(ProposalField, through='ProposalResponseField')
    name = models.CharField(max_length=100)  # Novo campo "name"
    documents = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Response #{self.pk} for Proposal #{self.proposal_model_id}"


class ProposalResponseField(models.Model):
    response_model = models.ForeignKey(ProposalResponse, on_delete=models.CASCADE)
    proposal_field = models.ForeignKey(ProposalField, on_delete=models.CASCADE)
    response_value = models.CharField(max_length=100)

    def __str__(self):
        return f"Response Field #{self.pk} for Response #{self.response_model_id}"
