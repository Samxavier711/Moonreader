from .models import Image
from .serializers import ImageSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .text import tex

class ImageUp(APIView):
	"""
		create a new image.
	"""
	def get(self, request, format=None):
		images = Image.objects.all()
		serializer = ImageSerializer(images, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = ImageSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			#tex.texx()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




def text_endpoint(request):
	if request.method == 'GET' or request.method=="POST":
		# Get the text data from the request
		text_data = request.POST.get('text_data', '')

		# Process the text data (e.g., save to a database, perform some operation)
		# ...

		# Return a JSON response as an example
		response_data = {'message': text_data}
		return JsonResponse(response_data)
	else:
		return JsonResponse({'error': 'Invalid request method'}, status=405)


    	# data=request.data
    	# print(data)
    	# if request.method == 'POST' and request.FILES['image']:
	    #     myfile = request.FILES['image']
	    #     fs = FileSystemStorage()
	    #     filename = fs.save(myfile.name, myfile)
	    #     uploaded_file_url = fs.url(filename)
	    #     return Response({'msg' : 'worked'}, status=status.HTTP_200_OK)
    	# return Response({'msg' : 'not worked'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)