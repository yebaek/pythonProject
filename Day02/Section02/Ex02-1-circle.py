# math 모듈 포함
import math

#get_area() 함수 정의
def get_area(radius): #(radius) 매개변수, 인자
    """반지름을 입력 받아서 원의 넓이를 반환하는 get_area() 함수"""
    area = math.pi * math.pow(radius, 2)
    return area

radius = 1.5 #반지름 1.5
print(radius)

#get_area() 함수 호출 결과를 area 변수에 저장
area = get_area(radius)
print(area)
print(get_area.__doc__) # Docstring 확인