#Ex1_하트그리기
#도형설정 : 리스트 활용
ver=[                  ]
length=        #사각형의 한 변의 길이 설정
def square() : #square함수 정의 : 사각형 그리기
    #한 변의 길이(length)만큼 앞으로 이동하고 오른쪽으로 90도 회전하기를 4회 반복

def drawRec(num) : #drawRec함수 정의 : 채우기 색 지정하여 사각형그리기
    '''
    1. 만약, num가 1이면, 채우기 색을 검정으로 설정하고 사각형 그리기
    그렇지 않고 만약, num가 2면, 채우기 색을 빨강으로 설정하고 사각형 그리기
    그렇지 않으면 채우기 색을 설정하지 않고 사각형 그리기
    2. 다음 사각형을 그리기 위해 한 변의 길이(length)만큼 앞으로 이동하기
    '''
 
#거북이 생성하기
import turtle   
turtle.title("도트 그림그리기 :  9X9 하트")
t=turtle.Turtle()
t.shape("turtle")
t.speed(0)
#초기 위치로 이동
t.penup()
t.goto(-300,300) 
t.pendown()
#도형그리기
for j in range(len(ver)):
    for i in ver[j]:
        drawRec(i)
    t.left(180)
    t.forward(length*len(ver[0]))
    t.left(90)
    t.forward(length)
    t.left(90)
turtle.done()













