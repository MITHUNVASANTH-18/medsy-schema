from mongoengine import Document, StringField, ValidationError

class Component(Document):
    name = StringField(required=True,unique=True)

    def clean(self):
        if not self.name.strip():
            raise ValidationError("Component name cannot be empty")

    def to_json(self):
        return {
            "id": str(self.id),
            "name": self.name
        }

    def update(self, **kwargs):
        self.clean()
        return super().update(**kwargs)
