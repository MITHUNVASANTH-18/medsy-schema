from mongoengine import ReferenceField,Document,StringField,DateTimeField
from Models.user_model import User
from Models.user_subscription_model import User_subscription
from datetime import datetime

class Transaction_detail(Document):
    user = ReferenceField(User,required=True,reverse_delete_rule=2)
    user_subscription = ReferenceField(User_subscription,required=True,reverse_delete_rule=2)
    transaction_time = DateTimeField(required=True,default=datetime.now())
    transaction_id = StringField(required=True)
    mode = StringField(required=True)
    amount_paid = StringField(required=True)
    status = StringField(required=True)

    def to_json(self):
        return {
        "id":str(self.id),
        "user":str(self.user.id) if self.user else None,
        "user_subscription":str(self.user_subscription.id) if self.user_subscription else None,
        "transaction_time":self.transaction_time,
        "transaction_id":self.transaction_id,
        "mode":self.mode,
        "amount_paid":self.amount_paid,
        "status":self.status
        }
    
    def with_key(self):
        return {
        "id":str(self.id),
        "user":self.user.to_json() if self.user else None,
        "user_subscription":self.user_subscription.to_json() if self.user_subscription else None,
        "transaction_time":self.transaction_time,
        "transaction_id":self.transaction_id,
        "mode":self.mode,
        "amount_paid":self.amount_paid,
        "status":self.status
        }

