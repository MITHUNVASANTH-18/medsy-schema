from mongoengine import Document,StringField,ReferenceField,ValidationError,BooleanField
from course_model import Course
from subject_model import Subject
from year_model import Year

class Layer_1(Document):
    course = ReferenceField(Course,required=True,reverse_delete_rule=2)
    subject = ReferenceField(Subject,required=True,reverse_delete_rule=2)
    year = ReferenceField(Year,required=True,reverse_delete_rule=2)
    name = StringField(required=True)
    content = StringField(required=True)
    image_url=StringField(required=True)
    has_prompt = BooleanField(required=True)
    
    def clean(self):
        if not self.name.strip():
            raise ValidationError("Layer_1 name cannot be empty")
    
    def to_json(self):
        return {
            "id": str(self.id),
            "course":str(self.course.id)  if self.course else None,
            "subject":str(self.subject.id) if self.subject else None,
            "year":str(self.year.id) if self.year else None,
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
            "name":self.name,
            "content":self.content,
            "image_url":self.image_url,
            "has_prompt":self.has_prompt
        }
    
    def update(self, **kwargs):
        self.clean()
        return super().update(**kwargs)