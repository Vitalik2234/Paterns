import hashlib

class PaymentCard:
    def __init__(self, owner, account_id, limit, repayment_days, security_code):
        self.owner = owner
        self.account_id = account_id
        self.limit = limit
        self.repayment_days = repayment_days
        self._security_code = self._hash_code(security_code)

    def _hash_code(self, code):
        return hashlib.sha256(code.encode()).hexdigest()

    @property
    def security_code(self):
        return self._security_code

    @security_code.setter
    def security_code(self, new_code):
        self._security_code = self._hash_code(new_code)

    def get_info(self):
        return {
            "owner": self.owner,
            "account_id": self.account_id,
            "limit": self.limit,
            "repayment_days": self.repayment_days,
            "security_code_hash": self._security_code,
        }
