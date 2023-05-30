from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

backstage = get_schema_view(
    openapi.Info(
        title="Backstage API",
        default_version='v1',
        # description="Backstage",
        # terms_of_service="",
        # contact=openapi.Contact(email="contact@snippets.local"),
        # license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)