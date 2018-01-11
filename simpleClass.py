# simpleClass.py

class Address:
    """nothing"""
    pass

pey = Address()

pey.name = "이지혜"
pey.phone = "010-1234-5678"
pey.email = "lionoffire@naver.com"
pey.hobby = "멍때리기"

for item in dir(pey):
    if '__' not in item:
        print(item, '\t: ', pey.__dict__[str(item)])


        
