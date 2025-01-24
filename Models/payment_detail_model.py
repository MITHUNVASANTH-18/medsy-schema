from mongoengine import ReferenceField,Document,StringField
from Models.user_model import User
from Models.user_subscription_model import User_subscription
from Models.transaction_detail_model import Transaction_detail

class Payment_detail(Document):
    user = ReferenceField(User,required=True,reverse_delete_rule=2)
    user_subscription = ReferenceField(User_subscription,required=True,reverse_delete_rule=2)
    transaction_detail = ReferenceField(Transaction_detail,required=True,reverse_delete_rule=2)
    net_amount = StringField(required=True)
    amount_with_tax = StringField(required=True)

    

    def to_json(self):
        return {
        "id":str(self.id),
        "user":str(self.user.id) if self.user else None,
        "user_subscription":str(self.user_subscription.id) if self.user_subscription else None,
        "transaction_detail":str(self.transaction_detail.id) if self.transaction_detail else None,
        "net_amount":self.net_amount,
        "amount_with_tax":self.amount_with_tax,
        }
    
    def with_key(self):
        return {
        "id":str(self.id),
        "user":self.user.to_json() if self.user else None,
        "user_subscription":self.user_subscription.to_json() if self.user_subscription else None,
        "transaction_detail":self.transaction_detail.to_json() if self.transaction_detail else None,
        "net_amount":self.net_amount,
        "amount_with_tax":self.amount_with_tax,
        }

