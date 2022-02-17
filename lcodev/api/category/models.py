from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
                #all modeled up, sql work her like this
                #     CREATE TABLE myapp_person (
                #     "id" serial NOT NULL PRIMARY KEY,
                #     "first_name" varchar(30) NOT NULL,
                #     "last_name" varchar(30) NOT NULL
                #       );

#
    def __str__(self):
        return self.name