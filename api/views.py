from django.http import JsonResponse

def UserProfileData(request, username):

    # do something with the your data
    data = {'type':'hello!'}

    # just return a JsonResponse
    return JsonResponse(data)
