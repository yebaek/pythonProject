'''

r (read mode) : 일기 전용 모드 | 파일 없으면 에러

경로
    절대경로 예) C:/pythonProject/Day07/Section13/hello.txt
    상대경로 예) ./upload/hello02.txt
        . -> 현재폴더
        .. -> 상위폴더
    최상위 경로(root) / 또는 C:/(윈도우OS)

'''

file = open('hello.txt', 'rt')
str = file.read()
print(str, end='')
file.close()