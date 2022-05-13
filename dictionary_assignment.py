나현 = {
    "name":"nahyun",
    "age":"20살",
    "birth":"3월7일",
    "gen":"W",
    "num":"010-8910-1441"
}
용복 = {
    "name":"yougbook",
    "age":"23살",
    "birth":"9월15일",
    "gen":"M",
    "num":"010-1234-5678"
}
원필 = {
    "name":"wonpil",
    "age":"29살",
    "birth":"4월28일",
    "gen":"M",
    "num":"010-5678-1234"
}

a = [1,2,3]
a[0:3] = [나현["name"],용복["name"],원필["name"]]

b = [1,2,3]
b[0:3] = [나현["age"],용복["age"],원필["age"]]

c = [1,2,3]
c[0:3] = [나현["birth"],용복["birth"],원필["birth"]]

d = [1,2,3]
d[0:3] = [나현["gen"],용복["gen"],원필["gen"]]

e = [1,2,3]
e[0:3] = [나현["num"],용복["num"],원필["num"]]

print("이름 리스트는 {}".format(a))
print("나이 리스트는 {}".format(b))
print("생일 리스트는 {}".format(c))
print("성별 리스트는 {}".format(d))
print("전화번호 리스트는 {}".format(e))


# 과제 수정 전 출력 코드
#print('나이 리스트는 ["{}","{}","{}"]'.format(나현["age"], 용복["age"], 원필["age"]))
#print('생일 리스트는 ["{}","{}","{}"]'.format(나현["birth"], 용복["birth"], 원필["birth"]))
#print('성별 리스트는 ["{}","{}","{}"]'.format(나현["gen"], 용복["gen"], 원필["gen"]))
#print('전화번호 리스트는 ["{}","{}","{}"]'.format(나현["num"], 용복["num"], 원필["num"]))
#print('이름 리스트는 ["{}","{}","{}"]'.format(나현["name"], 용복["name"], 원필["name"]))