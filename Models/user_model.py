from mongoengine import Document, ReferenceField, StringField
from Models.course_model import Course
from Models.year_model import Year
import re

class User(Document):
    course = ReferenceField(Course, required=True, reverse_delete_rule=2)
    year = ReferenceField(Year, required=True, reverse_delete_rule=2)
    username = StringField(required=True)
    email = StringField(required=True, unique=True, regex=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    password = StringField(required=True)

    def clean(self):
        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*?&]{8,}$', self.password):
            raise ValueError("Password must be at least 8 characters long and include at least one letter and one number.")

    def to_json(self):
        return {
            "id": str(self.id),
            "course": str(self.course.id) if self.course else None,
            "year": str(self.year.id) if self.year else None,
            "username": self.username,
            "email": self.email
        }

    def with_key(self):
        return {
            "id": str(self.id),
            "course": self.course.to_json() if self.course else None,
            "year": self.year.to_json() if self.year else None,
            "username": self.username,
            "email": self.email
        }
    
    def update(self, **kwargs):
        self.clean()
        return super().update(**kwargs)

