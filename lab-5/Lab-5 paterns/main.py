from credit_card import PaymentCard
from personal_info import UserInfo
from bank_info import FinancialDetails
from bank_customer import CustomerAccount
from dekorators import PremiumMember, PlatinumCard

def app():
    # Create PaymentCard object
    payment_card = PaymentCard("Alice Smith", "9876-5432-1098-7654", 10000, 45, "456")
    platinum_card = PlatinumCard(payment_card)

    # Create UserInfo and FinancialDetails objects
    user_info = UserInfo(name="Alice Smith", age=28, address="456 Maple Avenue")
    financial_info = FinancialDetails("Global Finance", "Alice Smith")
    financial_info.account_ids.append(payment_card.account_id)

    # Create CustomerAccount and PremiumMember objects
    customer_account = CustomerAccount(user_info, financial_info)
    premium_member = PremiumMember(customer_account)

    # Display results
    print("Payment Card Info:", platinum_card.get_info())
    print("Customer Account Info:", premium_member.get_info())

if __name__ == "__main__":
    app()
