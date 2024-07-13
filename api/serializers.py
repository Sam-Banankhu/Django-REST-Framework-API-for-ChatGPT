from rest_framework import serializers
# internals
from api.models import QueryResponder
from api import urls

class QueryResponderViewSerializer(serializers.ModelSerializer):
    class Meta:
        model =  QueryResponder
        fields = ("id", "_input", "_output")
        extra_kwargs = {
            "_output":{"read_only":True}
        }

        def create(self, validated_data):
            qr = QueryResponder(**validated_data)
            # _output = send_question_to_api(self.request_data)
            _output = urls.send_question_to_api(validated_data['_input'])
            qr._output = _output
            qr.save()
            
            return qr