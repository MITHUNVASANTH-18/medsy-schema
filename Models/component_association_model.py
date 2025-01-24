from mongoengine import Document,ReferenceField,ListField
from Models.course_model import Course
from Models.subject_model import Subject
from Models.year_model import Year
from Models.component_model import Component

class Component_association(Document):
    course = ReferenceField(Course,required=True,reverse_delete_rule=2)
    subject = ReferenceField(Subject,required=True,reverse_delete_rule=2)
    year = ReferenceField(Year,required=True,reverse_delete_rule=2)
    layer1 = ListField(ReferenceField(Component,reverse_delete_rule=2))
    layer2 = ListField(ReferenceField(Component,reverse_delete_rule=2))
    layer3 = ListField(ReferenceField(Component,reverse_delete_rule=2))

        
    def to_json(self):
        return {
            "id": str(self.id),
            "course":str(self.course.id) if self.course else None,
            "subject":str(self.subject.id) if self.subject else None,
            "year":str(self.year.id) if self.year else None,
            "layer1":[str(layer1_component.id) for layer1_component in self.layer1] if self.layer1 else None,
            "layer2":[str(layer2_component.id) for layer2_component in self.layer2] if self.layer2 else None,
            "layer3":[str(layer3_component.id) for layer3_component in self.layer3] if self.layer3 else None,
            
        }
    def with_key(self):
        return {
            "id": str(self.id),
            "course":self.course.to_json() if self.course else None,
            "subject":self.subject.to_json() if self.subject else None,
            "year":self.year.to_json() if self.year else None,
            "layer1":[layer1_component.to_json() for layer1_component in self.layer1] if self.layer1 else None,
            "layer2":[layer2_component.to_json() for layer2_component in self.layer2] if self.layer2 else None,
            "layer3":[layer3_component.to_json() for layer3_component in self.layer3] if self.layer3 else None,
            
        }
    
    def layer_key(self):
        return {
            "id": str(self.id),
            "course":str(self.course.id) if self.course else None,
            "subject":str(self.subject.id) if self.subject else None,
            "year":str(self.year.id) if self.year else None,
            "layer1":[layer1_component.to_json() for layer1_component in self.layer1] if self.layer1 else None,
            "layer2":[layer2_component.to_json() for layer2_component in self.layer2] if self.layer2 else None,
            "layer3":[layer3_component.to_json() for layer3_component in self.layer3] if self.layer3 else None,
            
        }
        
   