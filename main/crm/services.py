from .models import Apartment, Client, Manager


class ApartmentService:
    apartment = Apartment
    client = Client
    manager = Manager

    @classmethod
    def get_apartment(cls, **filters):
        try:
            return cls.apartment.objects.filter(**filters)
        except cls.model.DoesNotExist:
            raise

