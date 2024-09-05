from address import Address
from mailing import Mailing

to_address = Address(index="123456", city="Москва", street="Ленина", house="10", apartment="15")
from_address = Address(index="654321", city="Санкт-Петербург", street="Невский", house="5", apartment="20")

mail = Mailing(to_address=to_address, from_address=from_address, cost=350, track="TRACK123456789")

print(f"Отправление {mail.track} из {mail.from_address.index}, {mail.from_address.city}, {mail.from_address.street}, "
      f"{mail.from_address.house} - {mail.from_address.apartment} в {mail.to_address.index}, {mail.to_address.city}, "
      f"{mail.to_address.street}, {mail.to_address.house} - {mail.to_address.apartment}. "
      f"Стоимость {mail.cost} рублей.")