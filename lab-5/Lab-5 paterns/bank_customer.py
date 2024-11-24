class CustomerAccount:
    def __init__(self, user_info, financial_data):
        self.user_info = user_info
        self.financial_data = financial_data

    def get_info(self):
        account_info = {
            "user_info": vars(self.user_info),
            "financial_data": {
                "bank": self.financial_data.bank_name,
                "holder": self.financial_data.holder_name,
                "account_ids": self.financial_data.account_ids,
            },
            "recent_activity": (
                self.financial_data.get_transactions(self.financial_data.account_ids[0])
                if self.financial_data.account_ids
                else []
            ),
        }
        return account_info
