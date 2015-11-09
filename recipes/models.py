from django.db import models

# Create your models here.

"""
Hi, I'm writing a query in Django ORM that return all persons that have a skill set.

For example: all persons with "language == English" and "role == Manager"

An example of the SQL query can be as follows:

select person.name 
  from person 
 where exists
 		(select * 
 		  from skill 
 		 where skill.id = person.id
 		   and ((skill.type = 'language' and skill.value = 'English') and (skill.type = 'role' and skill.value = 'Manager')))

"""

"""
Well, I have this structure class model in Django
"""

class Person(models.Model):
	name = models.CharField(max_length=60)
	age = models.IntegerField()

	def __str__(self):
		return self.name

class Skill(models.Model):
	type = models.CharField(max_length=20)
	value = models.CharField(max_length=30)
	persons = models.ManyToManyField(Person)

	def __str__(self):
		return '{} - {} - {}'.format(self.type, self.value, ", ".join([i.name for i in self.persons.all()]))

"""
Records on table Person

| name   | age |
|--------|     |
| Arnold | 23  |
| Bull   | 24  | 
| John   | 25  |

Records on table Skill

| type  | value      | persons      |
|-------|------------|--------------|
| role  | Customer   | John, Bull   |
| role  | Manager    | John         |
| language | English    | Bull, Arnold |
| language | Portuguese | John, Bull   |

Use cases: 
  On filter role Customer and language English should return person Bull
  On filter role Customer and language Portuguese should return persons John and Bull
  On filter role Manager and language English should return no results

Is it possible to build a query that attend these use cases?

"""