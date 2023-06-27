from django.contrib import admin
from .models import Proposal, ProposalField, ProposalResponse, ProposalResponseField


class ProposalResponseFieldInline(admin.TabularInline):
    model = ProposalResponseField


class ProposalResponseInline(admin.TabularInline):
    model = ProposalResponse
    extra = 1


class ProposalFieldInline(admin.TabularInline):
    model = ProposalField


class ProposalAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_status', 'created_at')
    inlines = [ProposalFieldInline, ProposalResponseInline]

    def get_status(self, obj):
        proposal_response = ProposalResponse.objects.filter(proposal_model=obj).first()
        if proposal_response:
            return proposal_response.get_status_display()
        return ''

    get_status.short_description = 'Status'


class ProposalResponseAdmin(admin.ModelAdmin):
    inlines = [ProposalResponseFieldInline]


admin.site.register(Proposal, ProposalAdmin)
admin.site.register(ProposalField)
admin.site.register(ProposalResponse, ProposalResponseAdmin)
admin.site.register(ProposalResponseField)
