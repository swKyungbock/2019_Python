#20400 김선경
#파일명 : Ex4_입력받은정수부호에따라움직이기

#양수(100,100), 0(100,0), 음수(100,-100)
import turtle
t=turtle.Turtle()
t.shape("turtle")
turtle.title("김선경의 정수 부호에 따라 움직이는 프로그램")

t.penup()
t.goto(100,100)
t.write("거북이가 여기로 오면 양수입니다")

t.goto(100,0)
t.write("거북이가 여기로 오면 0입니다")

t.goto(100,-100)
t.write("거북이가 여기로 오면 음수입니다")

t.goto(0,0)

turtle.done()
