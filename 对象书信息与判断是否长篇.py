class Books:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def print_info(self):
        print(self.title)
        print(self.author)
        print(self.pages)
    def is_long_book(self):
        if self.pages > 400:
            print("是长篇小说")
        else:
            print("不是长篇小说")

book1=Books('《红楼梦》','曹雪芹',1200)
book2=Books('《小王子》','安托万·德·圣-埃克苏佩里',96)
book3=Books('《三体》','刘慈欣',500)
book1.print_info(),book1.is_long_book()
book2.print_info(),book2.is_long_book()
book3.print_info(),book3.is_long_book()