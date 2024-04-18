from dodo_is_api_client import AuthenticatedClient
from dodo_is_api_client.models import GetStaffMealsResponse200
import dodo_is_api_client.api.default.get_staff_meals as get_staff_meals
import datetime

client = AuthenticatedClient(base_url="https://api.dodois.io/dodopizza/ru", token="your_token")

with client as client:
    my_data: GetStaffMealsResponse200 = get_staff_meals.sync(client=client, 
                                                units='000d3a240c719a8711e68aba13f8ed18', 
                                                from_=datetime.date.today() - datetime.timedelta(days=1),
                                                to=datetime.date.today(),
                                                take=1000)
    print(my_data)