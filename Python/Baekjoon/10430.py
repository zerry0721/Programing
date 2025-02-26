# (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?
# (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?
# 세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.
#첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)
#첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.
a,b,c=map(int,input().split())
print((a+b)%c,((a%c)+(b%c))%c,(a*b)%c,((a%c)*(b%c))%c)

#숏코딩
# a,b,c=map(int,input().split());print(*[(a+b)%c]*2+[a*b%c]*2)
# 해설
#print(*[(a+b)%c]*2+[a*b%c]*2), 애초에 같은 결과가 두개씩이기 때문에 같은 연산을 두번 반복한 것.
#*는 리스트를 풀어주는 역할을 한다.
# 즉, [(a+b)%c]*2는 [(a+b)%c,(a+b)%c]가 되고, *를 사용하면 (a+b)%c,(a+b)%c가 된다.