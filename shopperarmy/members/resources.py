from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from .models import Member

class MemberResource(ModelResource):
    class Meta:
        queryset = Member.objects.all()
        resource_name = 'member'
        authorization = Authorization()