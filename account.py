

Class Account:
    def __init__(self, id, balance, name):
        self.id = id
        self.balance = balance
        self.name = name



    def deposit(self, amount):
        if amount <= 0:
            print("입금 금액을 확인해주세요")
            return 0
        else:
            self.balance += amount
            return self.balance


    def withdraw(self, amount):
        if amount > self.balance:
            print("잔액이 부족합니다.")
            return 0
        else:
            self.balance -= amount
            return self.balance

    def transfer(self, to, amount):
        pass

    def info(self):
        print(f"계좌 ID : {self.id}")
        print(f"이름 : {self.name}")
        print(f"잔액 : {self.balance}")

    def show_menu():
        print("------Menu-------")
        print("1. 계좌 계설")
        print("2. 입금")
        print("3. 출금")
        print("4. 송금")
        print("5. 계좌번호 전체 출력")
        print("6. 프로그램 종료")