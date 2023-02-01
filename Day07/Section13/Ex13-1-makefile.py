'''
파일 입출력(I/O - input/output)
    입력(input) 기존 파일 읽어들이는 것
    출력(output) 파일생성, 내용 추가를 말한다.
'''

# file = open('myfile.txt','wt')
# print('myfile.txt 파일이 생성되었습니다.')
# file.close()


with open('myfile.txt', 'wt') as file:
    print('myfile.txt 파일이 생성되었습니다.')