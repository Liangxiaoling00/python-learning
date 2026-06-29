import turtle as t
def gap(g):
    t.penup()
    t.fd(g)
    t.right(90)
    t.fd(g)
def cocolor(word):
    if word=="A":
        return "red"
    elif word=="b":
        return "orange"
    elif word=="C":
        return "yellow"
    elif word=="d":
        return "green"
    elif word=="E":
        return "blue"
    elif word=="F":
        return "purple"

def wordzzz(word,color):
    t.color(color)
    t.pendown()if word in["A","b","d","E","F"] else t.penup()
    t.fd(20)
    gap(5)
    t.pendown() if word in ["A", "b", "d"] else t.penup()
    t.fd(20)
    gap(5)
    t.pendown() if word in ["C", "b", "d","E" ] else t.penup()
    t.fd(20)
    gap(5)
    t.pendown() if word in ["C", "b", "d", "E","A","F"] else t.penup()
    t.fd(20)
    t.penup()
    t.fd(10)
    t.pendown() if word in ["C", "b", "A", "E","F"] else t.penup()
    t.fd(20)
    gap(5)
    t.pendown() if word in ["C", "A", "E", "F"] else t.penup()
    t.fd(20)
    gap(5)
    t.pendown() if word in [ "d", "A"] else t.penup()
    t.fd(20)
    t.penup()
    t.fd(5)
    t.left(90)
    t.fd(15)

words=["A","b","C","d","E","F",]
def main():
    t.setup(width=800, height=600)
    t.penup()
    t.pensize(5)
    t.fd(5)
    for i in words:
        cocolor(i)
        wordzzz(i,cocolor(i))
    t.hideturtle()
    t.done()
main()