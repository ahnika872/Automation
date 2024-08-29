from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 14", "+79161234567"),
    Smartphone("Samsung", "Galaxy S23", "+79161234568"),
    Smartphone("Google", "Pixel 7", "+79161234569"),
    Smartphone("Xiaomi", "Mi 11", "+79161234570"),
    Smartphone("Huawei", "P50 Pro", "+79161234571")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")