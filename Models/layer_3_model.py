from mongoengine import Document,StringField,ReferenceField,ValidationError,BooleanField
from Models.course_model import Course
from Models.subject_model import Subject
from Models.layer_1_model import Layer_1
from Models.layer_2_model import Layer_2
from Models.year_model import Year

class Layer_3(Document):
    course = ReferenceField(Course,required=True,reverse_delete_rule=2)
    subject = ReferenceField(Subject,required=True,reverse_delete_rule=2)
    year = ReferenceField(Year,required=True,reverse_delete_rule=2)
    layer1 = ReferenceField(Layer_1,required=True,reverse_delete_rule=2)
    layer2 = ReferenceField(Layer_2,reverse_delete_rule=2)
    name = StringField(required=True)
    content = StringField(required=True)
    image_url=StringField(required=True)
    has_prompt = BooleanField(required=True)

    def clean(self):
        if not self.name.strip():
            raise ValidationError("Layer_3 name cannot be empty")
        
    def to_json(self):
        return {
            "id": str(self.id),
            "course":str(self.course.id) if self.course else None,
            "subject":str(self.subject.id) if self.subject else None,
            "year":str(self.year.id) if self.year else None,
            "layer1":str(self.layer1.id) if self.layer1 else None,
            "layer2":str(self.layer2.id) if self.layer2 else None,
            "name":self.name,
            "content":self.content,
            "image_url":self.image_url,
            "has_prompt":self.has_prompt
        }
    
    def with_key(self):
        return {
            "id": str(self.id),
            "course":self.course.to_json() if self.course else None,
            "subject":self.subject.to_json() if self.subject else None,
            "year":self.year.to_json() if self.year else None,
            "layer1":self.layer1.to_json() if self.layer1 else None,
            "layer2":self.layer2.to_json() if self.layer2 else None,
            "name":self.name,
            "content":self.content,
            "image_url":self.image_url,
            "has_prompt":self.has_prompt
        }
        
    def update(self, **kwargs):
        self.clean()
        return super().update(**kwargs)