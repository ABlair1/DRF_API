from fizzbuzz.models import FizzBuzz


def get_new_fizzbuzz_data(request):
    """
    Returns an object containing the necessary field data to create a
    new FizzBuzz object.
    """
    return {
        "fizzbuzz_id": str(FizzBuzz.objects.count() + 1), # Next id
        # "useragent": request.META["HTTP_USER_AGENT"] if request.META["HTTP_USER_AGENT"] else None,
        "useragent": request.META["HTTP_USER_AGENT"],
        "message": request.data["message"],
        # creation_date field added at FizzBuzz creation
    }
