from django.db import models

# Create your models here.
class QueryResponder(models.Model):
    _input = models.TextField() # will keep user queries
    _output = models.TextField() # will keep gpt response

    class Meta:
        db_table = "t_query_responder"