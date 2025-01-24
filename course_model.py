from mongoengine import Document,StringField,BooleanField,ValidationError

class Course(Document):
    name = StringField(required=True,unique=True)
    duration = StringField(required=True)
    country = StringField(required=True)
    coin_value = StringField(required=True)
    has_prompt = BooleanField(required=True)

    def clean(self):
        if not self.duration.strip():
            raise ValidationError("Duration cannot be empty")
        if not self.name.strip():
            raise ValidationError("Course name cannot be empty")
        if not self.country.strip():
            raise ValidationError("Country cannot be empty")
        
    
    def to_json(self):
        return {
            "id": str(self.id),
            "name":self.name,
            "duration":self.duration,
            "country":self.country,
            "coin_value":int(self.coin_value),
            "has_prompt":self.has_prompt
        }
    
    def update(self, **kwargs):
        self.clean()
        return super().update(**kwargs)

