
from address import Address
from mailing import Mailing

mail = Mailing(from_address=Address(index=111111, city="Moscow", street="MKAD", house=1, apartment=13),
               to_address=Address(index=222222, city="Tomsk", street="Lenina", house=2, apartment=15),
               cost=5000,
               track=1234567890)

print(f"Отправление {mail.track} из {mail.from_address.index}, {mail.from_address.city}, {mail.from_address.street}, "
      f"{mail.from_address.house} - {mail.from_address.apartment} в {mail.to_address.index}, {mail.to_address.city}, "
      f"{mail.to_address.street}, {mail.to_address.house} -{mail.to_address.apartment}. Стоимость {mail.cost} рублей.")


