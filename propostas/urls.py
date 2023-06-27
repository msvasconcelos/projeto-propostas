from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProposalViewSet, ProposalFieldViewSet, ProposalResponseViewSet

router = DefaultRouter()
router.register(r'proposals', ProposalViewSet)
router.register(r'proposal-fields', ProposalFieldViewSet)
router.register(r'proposal-responses', ProposalResponseViewSet)
router.register(r'proposals/(?P<pk>\d+)', ProposalViewSet, basename='proposal-detail')

urlpatterns = [
    path('', include(router.urls)),
]