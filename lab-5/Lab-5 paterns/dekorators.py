class CardWrapper:
    def __init__(self, card):
        self.card = card

    def get_info(self):
        return self.card.get_info()


class PlatinumCard(CardWrapper):
    def get_info(self):
        card_info = super().get_info()
        card_info["privileges"] = "10% discount on all purchases"
        return card_info


class CorporateCard(CardWrapper):
    def get_info(self):
        card_info = super().get_info()
        card_info["privileges"] = "Exclusive perks for corporate users"
        return card_info


class PremiumMember:
    def __init__(self, account):
        self.account = account

    def get_info(self):
        account_info = self.account.get_info()
        account_info["membership"] = "Access to premium services and offers"
        return account_info
