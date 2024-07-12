from rest_framework import views, status
from rest_framework.response import Response
class QueryResponderView(views.APIView):
    serializer_class = QueryResponderViewSerializer

    def get(self, request, format = None):
        pass

    def post(self, request, format = None):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)