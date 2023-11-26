from .models import Apartment, Client, Manager


class ApartmentService:
    apartment = Apartment
    client = Client
    manager = Manager

    @classmethod
    def get_apartment(cls, **filters):
        try:
            return cls.apartment.objects.filter(**filters)
        except cls.apartment.DoesNotExist:
            raise

    @classmethod
    def get_manager(cls, **filters):
        try:
            return cls.manager.objects.filter(**filters)
        except cls.manager.DoesNotExist:
            raise
