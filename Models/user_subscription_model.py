from mongoengine import Document,StringField,ReferenceField,DateTimeField
from Models.coupon_model import Coupon
from Models.subscription_model import Subscription
from Models.user_model import User
# from Models.payment_detail_model import Payment_detail

class User_subscription(Document):
    # payment = ReferenceField(Payment_detail,required=True,reverse_delete_rule=2)
    user = ReferenceField(User,required=True,reverse_delete_rule=2)
    subscription = ReferenceField(Subscription,required=True,reverse_delete_rule=2)
    coupon = ReferenceField(Coupon,required=True,reverse_delete_rule=2)
    coins_redeemed=StringField(required=True)
    expiry = DateTimeField(required=True)

    def to_json(self):
        return {
            "id":str(self.id),
            # "payment":self.payment.to_json() if self.payment else None,
            "user":str(self.user.id) if self.user else None,
            "subscription":str(self.subscription.id) if self.subscription else None,
            "coupon":str(self.coupon.id) if self.coupon else None,
            "coins_redeemed":self.coins_redeemed,
            "expiry":self.expiry
        }
    
    def with_key(self):
        return {
            "id":str(self.id),
            # "payment":self.payment.to_json() if self.payment else None,
            "user":self.user.to_json() if self.user else None,
            "subscription":self.subscription.to_json() if self.subscription else None,
            "coupon":self.coupon.to_json() if self.coupon else None,
            "coins_redeemed":self.coins_redeemed,
            "expiry":self.expiry
        }