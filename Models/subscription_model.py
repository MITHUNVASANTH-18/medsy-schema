from mongoengine import Document,StringField,ReferenceField,ValidationError
from Models.course_model import Course
from Models.year_model import Year

class Subscription(Document):
    course = ReferenceField(Course,required=True,reverse_delete_rule=2)
    year = ReferenceField(Year,required=True,reverse_delete_rule=2)
    term_in_months = StringField(required=True)
    price = StringField(required=True)
    coins_threshold = StringField(required=True)
   
    def clean(self):
        if not self.term_in_months.strip():
            raise ValidationError("Term in months cannot be empty")
        if not self.price.strip():
            raise ValidationError("Price  cannot be empty")
        if not self.coins_threshold.strip():
            raise ValidationError("Coins threshold cannot be empty")
        

    def to_json(self):
        return {
            "id": str(self.id),
            "course":str(self.course.id) if self.course else None,
            "year":str(self.year.id) if self.year else None,
            "term_in_months":self.term_in_months,
            "price":self.price,
            "coins_threshold":self.coins_threshold
        }
    
    def with_key(self):
        return {
            "id": str(self.id),
            "course":self.course.to_json() if self.course else None,
            "year":self.year.to_json() if self.year else None,
            "term_in_months":self.term_in_months,
            "price":self.price,
            "coins_threshold":self.coins_threshold
        }
        
    def update(self, **kwargs):
        self.clean()
        return super().update(**kwargs)
    
    
   