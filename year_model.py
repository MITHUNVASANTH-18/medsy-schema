from mongoengine import Document,StringField,BooleanField,ValidationError,ReferenceField
from course_model import Course

class Year(Document):
    course = ReferenceField(Course,required=True,reverse_delete_rule=2)
    year = StringField(required=True)
    content = StringField(required=True)
    image_url = StringField(required=True)
    has_prompt = BooleanField(required=True)

    def clean(self):
        if not self.year.strip():
            raise ValidationError("Year cannot be empty")
       
    #response data year field changed as name for ui rendering purpose
    def to_json(self):
        return {
            "id":str(self.id),
            "course":str(self.course.id) if self.course else None,
            "name":self.year,
            "content":self.content,
            "image_url":self.image_url,
            "has_prompt":self.has_prompt
        }
    
    def with_key(self):
        return {
            "id":str(self.id),
            "course":self.course.to_json() if self.course else None,
            "name":self.year,
            "content":self.content,
            "image_url":self.image_url,
            "has_prompt":self.has_prompt
        }
        
    def update(self, **kwargs):
        self.clean()
        return super().update(**kwargs)

