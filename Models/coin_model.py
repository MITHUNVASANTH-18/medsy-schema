from mongoengine import Document,ReferenceField,IntField
from Models.course_model import Course
from Models.user_model import User

class Coin(Document):
    course = ReferenceField(Course,required=True,reverse_delete_rule=2)
    user = ReferenceField(User,required=True,reverse_delete_rule=2)
    count = IntField(required=True)

    def to_json(self):
        return {
            "id":str(self.id),
            "course":str(self.course.id) if self.course else None,
            "user":str(self.user.id) if self.user else None,
            "count":self.count
        }
    def with_key(self):
        return {
            "id":str(self.id),
            "course":self.course.to_json() if self.course else None,
            "user":self.user.to_json() if self.user else None,
            "count":self.count
        }