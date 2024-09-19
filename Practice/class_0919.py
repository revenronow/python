class 사람:
    def cry(self, sound):
        for i in sound:
            print(i)

    def call(self, name, phone):
        print(f'{name}에게 {phone} 발신 중')

    def 구구단(self, one, two):
        print(one * two)
    
    def 개인정보(self, name):
        center = "X" * (len(name) - 2)
        print(name[0] + center + name[-1])
        """
        center 변수에 name 변수 길이에서 2를 뺀(성과 마지막 이름 제외) 만큼 X를 곱한다
        name의 첫 번째 인덱스(성) 출력, center 출력, name의 마지막 인덱스(이름 끝 글자) 출력
        """
    
human = 사람()
# human.cry("엄마아아아")
# human.call("김철수", "010-1234-5678")
# human.구구단(3, 7)
# human.개인정보("유빛나라")

class 구구단:
    def print(self, num):
        for i in range(1, 10):
            print(f'{num} * {i} = {num*i}')

m = 구구단()
m.print(3)