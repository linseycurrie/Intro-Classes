class BankAccount:
    
    def __init__(self, input_holder_name, imput_balance, input_type):
        self.holder_name = input_holder_name
        self.balance = imput_balance
        self.type = input_type
        self._rates = {
            "personal": 10,
            "buisness": 50
        }
        
    def pay_in(self, amount):
        self.balance += amount

    def pay_monthly_fee(self):
        if self.type == "buisness":
            self.balance -= 50
        else:
            self.balance -= 10



# def get_account_name(account):
#     retun account["holder_name"]