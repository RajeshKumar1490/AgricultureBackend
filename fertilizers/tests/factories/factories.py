import factory
from fertilizers.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = "Rajesh"
    last_name = "rajesh"
    email = factory.sequence(lambda n: "rajesh_%d@gmail.com" %(n + 1))
    username = factory.sequence(lambda n: "user_%d" %(n + 1))
