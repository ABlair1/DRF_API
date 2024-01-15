from rest_framework import serializers
from fizzbuzz.models import FizzBuzz

MSG_ERROR = {"message": ["This is the only field allowed in the request body."]}
HEADER_ERROR = ["POST request must have a valid HTTP User-Agent header"]


class FizzBuzzSerializer(serializers.ModelSerializer):
    class Meta:
        model = FizzBuzz
        fields = [
            "fizzbuzz_id",
            "creation_date",
            "useragent",
            "message",
        ]


class FizzBuzzCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FizzBuzz
        fields = [
            "message",
        ]

    def validate_fields(self, data):
        """
        Validates that data only has the message field for a Fizzbuzz
        object.
        """
        if len(data) > 1 or "message" not in data:
            raise serializers.ValidationError(MSG_ERROR) # Default status 400
    
    def validate_headers(self, request):
        """
        Validates that request has required headers. POST requests
        require the User-Agent header to create a FizzBuzz object.
        """
        if "HTTP_USER_AGENT" not in request.META:
            raise serializers.ValidationError(HEADER_ERROR) # Default status 400
