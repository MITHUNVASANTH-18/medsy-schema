from mongoengine import Document,StringField,ReferenceField,DictField
from Models.course_model import Course
from Models.subject_model import Subject
from Models.layer_1_model import Layer_1
from Models.year_model import Year

class Flashcard(Document):
    course = ReferenceField(Course,required=True,reverse_delete_rule=2)
    subject = ReferenceField(Subject,required=True,reverse_delete_rule=2)
    year = ReferenceField(Year,required=True,reverse_delete_rule=2)
    layer1 = ReferenceField(Layer_1,required=True,reverse_delete_rule=2)
    type = StringField(required=True)
    content = DictField(required=True)


   
    def to_json(self):
        return {
            "id": str(self.id),
            "course":str(self.course.id) if self.course else None,
            "subject":str(self.subject.id) if self.subject else None,
            "year":str(self.year.id) if self.year else None,
            "layer1":str(self.layer1.id) if self.layer1 else None,
            "type":self.type,
            "content":self.content,
        }
    
    def with_key(self):
        return {
            "id": str(self.id),
            "course":self.course.to_json() if self.course else None,
            "subject":self.subject.to_json() if self.subject else None,
            "year":self.year.to_json() if self.year else None,
            "layer1":self.layer1.to_json() if self.layer1 else None,
            "type":self.type,
            "content":self.content,
        }
    
    