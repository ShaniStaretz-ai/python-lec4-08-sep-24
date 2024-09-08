# number: int = int(input("enter number:\n"));
# if number % 7 == 0:
#     print("7-boom");
# else:
#     print("not-7-boom")
#
# asarot: int = number // 10
# ahadot: int = number % 10;
#
# print("asarot:", asarot)
# print("ahadot:", ahadot)

place_in_car = 5

passengers: int = int(input("enter number of people:\n"));
cars=passengers // place_in_car
print("full cars:", passengers // place_in_car)
if passengers % place_in_car != 0:
    cars+=1
    print("not full cars:", 1)
else:
    print("no full cars")

print("need total cars:",cars)
