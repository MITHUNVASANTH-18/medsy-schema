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
    layer1 = ReferenceField(Layer_1,reverse_delete_rule=2)
    layer2 = ReferenceField(Layer_2,required=True,reverse_delete_rule=2)
    name = StringField(required=True)
    meta_title = StringField()
    meta_image_url = StringField()
    meta_description = StringField()
    meta_content = StringField()
    has_prompt = BooleanField()
    key = StringField(required=True,unique=True)
    competency_key = StringField()

    def clean(self):
        if not self.name.strip():
            raise ValidationError("Layer_3 name cannot be empty")
        if not self.key.strip():
            raise ValidationError("key cannot be empty")
        
    def to_json(self):
        return {
            "id": str(self.id),
            "course":str(self.course.id) if self.course else None,
            "subject":str(self.subject.id) if self.subject else None,
            "year":str(self.year.id) if self.year else None,
            "layer1":str(self.layer1.id) if self.layer1 else "",
            "layer2":str(self.layer2.id) if self.layer2 else None,
            "name":self.name,
            "meta_title":self.meta_title,
            "meta_image_url":self.meta_image_url,
            "meta_description":self.meta_description,
            "meta_content":self.meta_content,
            "has_prompt":self.has_prompt,
            "key":self.key,
            "competency_key":self.competency_key
        }
    
    def with_key(self):
        return {
            "id": str(self.id),
            "course":self.course.to_json() if self.course else None,
            "subject":self.subject.to_json() if self.subject else None,
            "year":self.year.to_json() if self.year else None,
            "layer1":self.layer1.to_json() if self.layer1 else "",
            "layer2":self.layer2.to_json() if self.layer2 else None,
            "name":self.name,
            "meta_title":self.meta_title,
            "meta_image_url":self.meta_image_url,
            "meta_description":self.meta_description,
            "meta_content":self.meta_content,
            "has_prompt":self.has_prompt,
            "key":self.key,
            "competency_key":self.competency_key

        }
        
    def update(self, **kwargs):
        self.clean()
        return super().update(**kwargs)