class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"عنوان کتاب: {self.title}")
        print(f"نویسنده: {self.author}")
        print(f"قیمت: {self.price} تومان")
        print("-" * 30)

    def apply_discount(self, percent):
        
        discount_amount = self.price * (percent / 100)
        self.price -= discount_amount




book1 = Book("پایتون پیشرفته", "علی رضایی", 200000)
book2 = Book("هوش مصنوعی", "سمیه محمدی", 150000)

print("اطلاعات اولیه:")
book1.display_details()
book2.display_details()

# تخفیف
book1.apply_discount(10)   # 10 درصد
book2.apply_discount(15)   # 15 درصد

print("بعد از اعمال تخفیف:")
book1.display_details()
book2.display_details()
