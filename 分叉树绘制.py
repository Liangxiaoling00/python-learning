import turtle as t

def tree(long):
    if long < 10:
        return
    t.pendown()
    t.fd(long)
    t.left(25)
    tree(long*0.7)
    t.right(50)
    tree(long*0.7)
    t.left(25)
    t.penup()
    t.back(long)


def main():
    t.setup(1200,600)
    t.goto(0,0)
    t.left(90)
    tree(80)
    t.done()
main()