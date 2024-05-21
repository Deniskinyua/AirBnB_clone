#!/usr/bin/python3
"""
class BaseModel acts as a base model for other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        Task 1 -> Constructor: initializes id, created_at & updated_at
        Task 2 -> update to cater for args & kwargs
        """
        fmt = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, fmt))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def save(self):
        """updates updated_at with the current datetime"""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """Returns a dict -> all keys/values of __dict__ instance"""
        instanceDict = self.__dict__.copy()
        instanceDict["__class__"] = self.__class__.__name__
        instanceDict["created_at"] = self.created_at.isoformat()
        instanceDict["updated_at"] = self.updated_at.isoformat()
        return instanceDict

    def __str__(self):
        """Prints [<class name>] (<self.id>) <self.__dict__>"""
        className = self.__class__.__name__
        return "[{}] ({}) {}".format(className, self.id, self.__dict__)
