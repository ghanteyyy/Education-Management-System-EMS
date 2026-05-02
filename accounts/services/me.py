from accounts import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiExample


@extend_schema(
    request=None,
    summary="Get Current User",
    description="Retrieve the currently authenticated user's information.",
    responses=serializers.MeSerializer,
    examples=[
        OpenApiExample(
            "Example Response",
            value={
                "id": 1,
                "name": "John Doe",
                "email": "john.doe@example.com",
                "gender": "male",
                "date_of_birth": "1990-01-01",
                "profile_image": "http://example.com/profile.jpg"
            },
            response_only=True,
        )
    ]
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me(request):
    serializer = serializers.MeSerializer(request.user)
    return Response(serializer.data)
