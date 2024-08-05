class BankAccount:

    def __init__(self, userName, userBalance=0):
        self.userName = userName
        self.userBalance = userBalance

    def deposit(self, value):
        if(value > 0):
            self.userBalance += value
        else:
            return "Please, deposit only valid values"
    
    def withdrawal(self, value):
        if(value < self.getUserBalance()):
            self.userBalance -= value
        else:
            return "Insufficient balance for this transaction"

    def getUserBalance(self):
        return self.userBalance
    
    def getUserName(self):
        return self.userName
    
    