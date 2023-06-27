from django.contrib import admin
from .models import Proposal, ProposalResponse, ProposalField


class ProposalFieldInline(admin.TabularInline):
    model = ProposalField


@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    inlines = [ProposalFieldInline]
    list_display = ['id', 'title', 'created_at']


@admin.register(ProposalResponse)
class ProposalResponseAdmin(admin.ModelAdmin):
    list_display = ['id', 'proposal_title', 'name', 'documents', 'status']

    def proposal_title(self, obj):
        return obj.proposal_model.title

    proposal_title.short_description = 'Proposal Title'


