from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Services
from .serializers import ServicesSerializer
from rest_framework.generics import get_object_or_404


class ServicesView(APIView):
    def get(self, request):
        services = Services.objects.all()
        serializer = ServicesSerializer(services, many=True)
        return Response({"services": serializer.data})


    def post(self, request):
        services = request.data.get('services')
        # Create an article from the above data
        serializer = ServicesSerializer(data=services)
        if serializer.is_valid(raise_exception=True):
            services_saved = serializer.save()
        return Response({"success": "Services '{}' created successfully".format(services_saved.title)})



    def put(self, request, pk):
        saved_services = get_object_or_404(Services.objects.all(), pk=pk)
        data = request.data.get('services')
        serializer = ServicesSerializer(instance=saved_services, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            services_saved = serializer.save()
        return Response({
            "success": "Services '{}' updated successfully".format(services_saved.title)
        })



    def delete(self, request, pk):
       # Get object with this pk
       services = get_object_or_404(Services.objects.all(), pk=pk)
       services.delete()
       return Response({
           "message": "Article with id `{}` has been deleted.".format(pk)
       }, status=204)

