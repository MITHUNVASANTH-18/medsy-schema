from mongoengine import Document,StringField,BooleanField,ValidationError

class Course(Document):
    name = StringField(required=True,unique=True)
    duration = StringField(required=True)
    country = StringField(required=True)
    coin_value = StringField(required=True)
    meta_title = StringField()
    meta_image_url = StringField()
    meta_description = StringField()
    meta_content = StringField()
    has_prompt = BooleanField(required=True)
    key = StringField(required=True,unique=True)

    def clean(self):
        if not self.duration.strip():
            raise ValidationError("duration cannot be empty")
        if not self.name.strip():
            raise ValidationError("course name cannot be empty")
        if not self.country.strip():
            raise ValidationError("country cannot be empty")
        if not self.key.strip():
            raise ValidationError("key cannot be empty")
        
    
    def to_json(self):
        return {
            "id": str(self.id),
            "name":self.name,
            "duration":self.duration,
            "country":self.country,
            "coin_value":int(self.coin_value),
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

