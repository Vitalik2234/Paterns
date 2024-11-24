class FinancialDetails:
    def __init__(self, bank_name, holder_name):
        self.bank_name = bank_name
        self.holder_name = holder_name
        self.account_ids = []
        self.payment_history = {}

    def get_transactions(self, account_id):
        return [f"Activity {i+1} on account {account_id}" for i in range(3)]
