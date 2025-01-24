from mongoengine import Document,StringField,ValidationError,EnumField

class Model(Document):
    name = StringField(required=True,unique=True)
    api_key = StringField(required=True)
    type = StringField(required=True)
    provider = StringField(choices=['gemini','openai','claude'],required=True)

    
    def clean(self):
        if not self.name.strip():
            raise ValidationError("Model name cannot be empty")
        if not self.api_key.strip():
            raise ValidationError("Api key cannot be empty")
        if not self.type.strip():
            raise ValidationError("model type cannot be empty")

    def to_json(self):
        return {
            "id": str(self.id),
            "name":self.name,
            "api_key":self.api_key,
            "type":self.type,
            "provider":self.provider
        }
    
        
        
    def update(self, **kwargs):
        self.clean()
        return super().update(**kwargs)