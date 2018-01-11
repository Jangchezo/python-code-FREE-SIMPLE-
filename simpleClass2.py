# simpleClass2.py

class Person:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


pey = Person('이지헤', '010-1234-5678', 'lionoffire@naver.com')

             
print(pey.name)
print(pey.phone)
print(pey.email)
