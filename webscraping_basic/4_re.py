# 4_re.md 참고

import re

p = re.compile("ca.e")


def print_match(m):
    if m:
        print("m.group() : ", m.group()) # 일치하는 문자열 반환
        print("m.string : ", m.string)   # 입력받은 문자열 반환
        print("m.start() : ", m.start()) # 일치하는 문자열의 시작 index 반환
        print("m.end() : ", m.end())     # 일치하는 문자열의 끝 index 반환
        print("m.span() : ", m.span())   # 일치하는 문자열의 시작 / 끝 index 반환
    else:
        print("매칭되지 않음")

# match : 주어진 문자열이 처음부터 일치하는지 확인 (맨 처음 발견하는 단어)
m = p.match("case")
print_match(m)

# search : 주어진 문자열 중에 일치하는게 있는지 확인 (맨 처음 발견하는 단어)
m = p.search("good care")
print_match(m)

# findall : 일치하는 모든 것을 리스트로 반환
lst = p.findall("good care cafe")
print(lst)