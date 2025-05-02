from backend import create_account
from backend import deposit
from backend import withdraw
from backend import get_balance
from backend import modify_account
from backend import delete_account


print(create_account("damiomabuwa", "Damire123"))
print(deposit("damiomabuwa", 100.0))
print(withdraw("damiomwabuwa", 40.0))
print("Balance:", get_balance("damiomabuwa"))
print(modify_account("damiomabuwa", new_password="iCode1234"))
print(delete_account("damiomabuwa"))

