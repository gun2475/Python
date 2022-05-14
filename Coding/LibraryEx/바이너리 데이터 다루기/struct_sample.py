import struct
with open('E:\Python\Coding\LibraryEx\바이너리 데이터 다루기\ouput', 'rb') as f:
    chunk = f.read(16)
    result = struct.unpack('dicccc', chunk)
    print(result)

# unpack() 함수의 첫 번째 인수 'dicccc' double형 1개, int형 1개,char형 4개를 뜻한다. 앞의 C프로그램에서 save_type 구조체는 double형 1개, int형 1개, char형 1개로 이루어지지만 unpack()은 구조체 전체 길이인 16바이트 크기에 맞게 설정해야한다.

# save_type 구조체의 길이가 16바이트인 이유는 C 구조체의 특징 때문으로, 가장 큰 double형의 크기 8바이트의 배수로 구조체의 길이가 결정되기 때문이다. 따라서 이 구조체의 크기는 16바이트가 되고 실제 데이터 13바이트와 3바이트 널값으로 이루어진다.
