

class Account:
    def __init__(self, id, balance, name):
        self.id = id
        self.balance = balance
        self.name = name



    def deposit(self, amount):
        if amount <= 0:
            print("입금 금액을 확인해주세요")
            return False
        self.balance += amount
        print(f"{amount}원 입금")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("출금 금액을 확인해주세요")
            return False
        elif amount > self.balance:
            print("잔액이 부족합니다.")
            return False
        else:
            self.balance -= amount
            print(f"{amount}원 출금")
            return True



    def info(self):
        print(f"계좌 ID : {self.id}")
        print(f"이름 : {self.name}")
        print(f"잔액 : {self.balance}")


accounts = {}



def show_menu():
    print("------Menu-------")
    print("1. 계좌 계설")
    print("2. 입금")
    print("3. 출금")
    print("4. 송금")
    print("5. 계좌확인")
    print("6. 프로그램 종료")


def make_account():
    print("[계좌 계설]")
    try:
        id = int(input("계좌ID:(숫자로 입력해 주세요) :"))
        if id in accounts:
            print("이미 존재하는 계좌입니다.")
            return

        name = input("이름: ")
        balance = int(input("초기 금액:"))
        accounts[id] = Account(id, balance, name)
        print("계좌가 개설되었습니다")
    except ValueError:
        print("\n 입력형식이 올바르지 않습니다. \n")



def deposit():
    print("[입급]")
    try:
        id = int(input("계좌 ID: "))
        if id not in accounts:
            print("계좌가 존재하지 않습니다")
            return

        amount = int(input("입금 금액: "))
        accounts[id].deposit(amount)
    except ValueError:
        print("\n 입력형식이 올바르지 않습니다. \n")


def withdraw():
    print("[출금]")
    try:
        id = int(input("계좌 ID: "))
        if id not in accounts:
            print("계좌가 존재하지 않습니다.")
            return

        amount = int(input("출금 금액: "))
        accounts[id].withdraw(amount)
    except ValueError:
        print("입력 형식이 올바르지 않습니다.")



def transfer():
    print("[송금]")
    try:
        from_id = int(input("보내는 계좌 ID: "))
        to_id = int(input("받는 계좌 ID: "))
        amount = int(input("송금 금액: "))

        if from_id not in accounts:
            print("보내는 계좌가 존재하지 않습니다.")
            return
        if to_id not in accounts:
            print("받는 게좌가 존재하지 않습니다")

        if amount <= 0:
            print("송금 금액 확인 요망")
            return

        sender = accounts[from_id]
        receiver = accounts[to_id]

        if sender.withdraw(amount):
            receiver.deposit(amount)
            print("송금 완료")

    except ValueError:
        print("\n 입력형식이 올바르지 않습니다. \n")



def show_accounts():
    print("[계좌 확인]")
    if not accounts:
        print("등록된 계좌가 없습니다.")
        return

    for acc in accounts.values():
        acc.info()




def main():
    while True:
        show_menu()
        choice = input("메뉴 선택: ").strip()

        if choice == "1":
            make_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            transfer()
        elif choice == "5":
            show_accounts()
        elif choice == "6":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. (1~6)")


if __name__ == "__main__":
    main()
