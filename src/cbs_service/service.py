from common.date_and_time import get_current_time
from orm.exceptions import CustomerNotFoundHydrationError


def get_current_time_service():
    print(get_current_time())


def raise_error():
    raise CustomerNotFoundHydrationError("Customer not found! 😮")
