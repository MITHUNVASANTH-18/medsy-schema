from mongoengine import ReferenceField,Document,BooleanField
from Models.flashcard_model import Flashcard
from Models.user_model import User

class Flashcard_queue(Document):
    flashcard = ReferenceField(Flashcard,required=True,reverse_delete_rule=2)
    user = ReferenceField(User,required=True,reverse_delete_rule=2)
    is_triggered = BooleanField(required=True)


    def to_json(self):
        return {
            "id": str(self.id),
            "flashcard":str(self.flashcard.id) if self.flashcard else None,
            "user":str(self.user.id) if self.user else None,
            "is_triggered":self.is_triggered,
        }
    
    def with_key(self):
        return {
            "id": str(self.id),
            "flashcard":self.flashcard.to_json() if self.flashcard else None,
            "user":self.user.to_json() if self.user else None,
            "is_triggered":self.is_triggered,
        }