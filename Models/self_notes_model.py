from mongoengine import Document, ReferenceField, StringField,DateTimeField
from datetime import datetime
from Models.user_model import User

class Self_note(Document):
    user = ReferenceField(User,required=True,reverse_delete_rule=2)
    title = StringField(required=True)
    notes_content = StringField(required=True)
    date = DateTimeField(required=True,default=datetime.now())


    
    def to_json(self):
        return {
            "id": str(self.id),
            "user": str(self.user.id),
            "title":self.title,
            "notes_content":self.notes_content,
            "date":self.date
        }

    def with_key(self):
        return {
            "id": str(self.id),
            "user": self.user.to_json() if self.user else None,
            "title":self.title,
            "notes_content":self.notes_content,
            "date":self.date
        }
    
    def update(self, **kwargs):
        self.clean()
        return super().update(**kwargs)

