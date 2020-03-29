from rest_framework import serializers
from snippets.models import User,Activity

class UserSerializer(serializers.Serializer):
	vat_id = serializers.CharField(max_length=200)
	name = serializers.CharField(max_length=200)
	address = serializers.CharField(max_length=200)
	class meta :
		model = User
		fields = '__all__'


class ActivitySerializer(serializers.Serializer):
	uid = UserSerializer(read_only=True)
	startdate = serializers.DateTimeField()
	enddate = serializers.DateTimeField()
	class meta:
		model = Activity
		fields = ['startdate','enddate','uid']

