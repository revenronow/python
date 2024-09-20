"""
class 사람:
    def __init__(self, 이름):
        # print("응애응애")
        # print(f'{이름} 님이 태어났습니다.')
        # self.연도 = 연도
        self.성 = 이름[0]
        self.이름 = 이름[1:]

human = 사람("유종훈")
# human.연도
human.성
human.이름
"""

class 사람:
    def __init__(self, *친구):
        self.친구0 = 친구[0]
        self.친구1 = 친구[1]
        self.친구 = 친구[:]

human = 사람("유종훈", "조현호")
human.친구0