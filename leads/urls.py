
from django.urls import path
from django.contrib import admin
from leads.views import( lead_create, lead_delete, lead_list,lead_detail, lead_update,
LeadListView,LeadDetailView,LeadCreateView,LeadUpdateView,LeadDeleteView
)
app_name="leads"
urlpatterns = [
    path('',LeadListView.as_view(),name="lead_list"),
    path('<int:pk>/',LeadDetailView.as_view(),name="lead_detail"),
    path('<int:pk>/update/',LeadUpdateView.as_view(),name="lead_update"),
    path('<int:pk>/delete/',LeadDeleteView.as_view(),name="lead_delete"),
    path('create-new-lead/',LeadCreateView.as_view(),name="lead_create")
]