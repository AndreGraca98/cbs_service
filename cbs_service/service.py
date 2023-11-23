from common.date_and_time import get_current_time
from orm.exceptions import CustomerNotFoundHydrationError

print(get_current_time())
raise CustomerNotFoundHydrationError("Customer not found! 😮")
