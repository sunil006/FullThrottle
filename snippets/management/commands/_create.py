import factory  
import factory.django
from snippets.models import User,Activity
from faker import Faker

class UserFactory(factory.django.DjangoModelFactory):  
    class Meta:
        model = User
    factory.Faker._DEFAULT_LOCALE='en_IE'
    vat_id=factory.Faker('vat_id')
    name = factory.Faker('name')
    address = factory.Faker('address')
    
class ActivityFactory(factory.django.DjangoModelFactory):  
    class Meta:
        model = Activity
    factory.Faker._DEFAULT_LOCALE='en_IE'
    uid=UserFactory()
    startdate = factory.Faker('date_time')
    enddate = factory.Faker('date_time')
    
