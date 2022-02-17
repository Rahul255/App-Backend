from django.db import migrations
from api.user.models import CustomUser


class Migration(migrations.Migration):
    #pass all the apps which are we created 
    def seed_data(apps, schema_editor):
        user = CustomUser(name="rahul",
                          email="rahulmohan255@gmail.com",
                          is_staff=True,
                          is_superuser=True,
                          phone="98647773",
                          gender="Male"
                          )
        user.set_password("rahul")
        user.save()

    dependencies = [
        #it its dependent on another dependencies they only we need to add that, otherwise just skip this
    ]

    operations = [
        migrations.RunPython(seed_data),#ask python to run this seed_data function
    ]