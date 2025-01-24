from mongoengine import Document,StringField,ReferenceField,ValidationError,DateTimeField
from Models.course_model import Course

class Coupon(Document):
    course = ReferenceField(Course,required=True,reverse_delete_rule=2)
    name = StringField(required=True)
    discount_in_percentage = StringField()
    discount_in_flat = StringField()
    max_discount_in_price = StringField(required=True)
    expires = DateTimeField(required=True)
    count = StringField(required=True)

    

    def clean(self):
        if not self.name.strip():
            raise ValidationError("Coupon name cannot be empty")
        

    def to_json(self):
        return {
            "id": str(self.id),
            "course":str(self.course.id) if self.course else None,
            "name":self.name,
            "discount_in_percentage":self.discount_in_percentage,
            "discount_in_flat":self.discount_in_flat,
            "max_discount_in_price":self.max_discount_in_price,
            "expires":self.expires,
            "count":self.count
        }
    
    def with_key(self):
        return {
            "id": str(self.id),
            "course":self.course.to_json() if self.course else None,
            "name":self.name,
            "discount_in_percentage":self.discount_in_percentage,
            "discount_in_flat":self.discount_in_flat,
            "max_discount_in_price":self.max_discount_in_price,
            "expires":self.expires,
            "count":self.count
        }
        
    def update(self, **kwargs):
        self.clean()
        return super().update(**kwargs)
    
    
   