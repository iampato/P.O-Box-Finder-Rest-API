from tastypie.resources import ModelResource
from api.models import School
from tastypie.authorization import Authorization

class NoteResource(ModelResource):
    class Meta:
        queryset = School.objects.all()
        resource_name = 'school'
        authorization = Authorization()
        fields = ['name', 'box', 'mapurl']