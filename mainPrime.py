
class User():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def userAut(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        if self.age == "root" and self.age >= 18:
            print("Добро пожаловать на сервер БЕЗУМНЫЕ ЗОМБИ\nБЕСПЛАТНАЯ ВИПКА\nДОНАТ ЧЕРЕЗ ВК")

def main():
    users = User(" ", 0)
    users.userAut()

if __name__ == "__main__":
    main()
    