
from django.db import models
from django.db.models import Transform
# Create your models here.

class Task(models.Model):
	name = models.CharField(max_length=60)
	days = models.IntegerField()

	def __str__(self):
		return self.name

class MD5Value(Transform):
    lookup_name = 'md5'
    output_field = models.CharField()

    def as_sql(self, compiler, connectino):
        lhs, params = compiler.compile(self.lhs)
        return "MD5(cast(%s as text))"  % lhs, params

models.AutoField.register_lookup(MD5Value)

class AbsoluteValue(Transform):
    lookup_name = 'abs'

    def as_sql(self, compiler, connection):
        lhs, params = compiler.compile(self.lhs)
        return "ABS(%s)" % lhs, params
        
models.IntegerField.register_lookup(AbsoluteValue)

"""
How to use
 


Students.objects.get(pk__md5=md5)
"""