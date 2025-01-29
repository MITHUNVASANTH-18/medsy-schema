from mongoengine import Document,StringField,BooleanField,ValidationError,ReferenceField
from Models.course_model import Course

class Year(Document):
    course = ReferenceField(Course,required=True,reverse_delete_rule=2)
    year = StringField(required=True)
    meta_title = StringField()
    meta_image_url = StringField()
    meta_description = StringField()
    meta_content = StringField()
    has_prompt = BooleanField(required=True)
    key = StringField(required=True,unique=True)

    def clean(self):
        if not self.year.strip():
            raise ValidationError("year cannot be empty")
        if not self.key.strip():
            raise ValidationError("key cannot be empty")
       
    #response data year field changed as name for ui rendering purpose
    def to_json(self):
        return {
            "id":str(self.id),
            "course":str(self.course.id) if self.course else None,
            "name":self.year,
            "meta_title":self.meta_title,
            "meta_image_url":self.meta_image_url,
            "meta_description":self.meta_description,
            "meta_content":self.meta_content,
            "has_prompt":self.has_prompt,
            "key":self.key
        }
    
    def with_key(self):
        return {
            "id":str(self.id),
            "course":self.course.to_json() if self.course else None,
            "name":self.year,
            "meta_title":self.meta_title,
            "meta_image_url":self.meta_image_url,
            "meta_description":self.meta_description,
            "meta_content":self.meta_content,
            "has_prompt":self.has_prompt,
            "key":self.key
        }
        
    def update(self, **kwargs):
        self.clean()
        return super().update(**kwargs)

