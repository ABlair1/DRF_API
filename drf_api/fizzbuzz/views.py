from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from fizzbuzz.helpers import get_new_fizzbuzz_data
from fizzbuzz.models import FizzBuzz
from fizzbuzz.serializers import FizzBuzzSerializer, FizzBuzzCreateSerializer


@api_view(["GET", "POST"])
def fizzbuzz_list(request):
    """
    Return a list of all FizzBuzz objects, or create a new FizzBuzz
    object.
    """
    if request.method == "GET":
        # Retrieve and return list of all
        fb_list = FizzBuzz.objects.all()
        fb_serializer = FizzBuzzSerializer(fb_list, many=True)
        return Response(fb_serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "POST": # Create new
        # Validate request header and data
        req_serializer = FizzBuzzCreateSerializer(data=request.data)
        req_serializer.validate_headers(request=request)
        req_serializer.validate_fields(data=request.data)
        if not req_serializer.is_valid():
            return Response(
                req_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        # Get data for new FizzBuzz
        fb_data = get_new_fizzbuzz_data(request)
        fb_serializer = FizzBuzzSerializer(data=fb_data)

        # Validate and create Fizzbuzz
        if fb_serializer.is_valid():
            fb_serializer.save()
            return Response(
                fb_serializer.data,
                status=status.HTTP_201_CREATED
            )
        
        # Return server error if unable to validate and create FizzBuzz
        return Response(
            fb_serializer.errors,
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(["GET"])
def fizzbuzz_single(request, fizzbuzz_id):
    """
    Return the FizzBuzz object with the specified id.
    """
    # Get FizzBuzz with fizzbuzz_id
    try:
        fb = FizzBuzz.objects.get(fizzbuzz_id=str(fizzbuzz_id))
    except FizzBuzz.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        fb_serializer = FizzBuzzSerializer(fb)
        return Response(fb_serializer.data, status=status.HTTP_200_OK)
