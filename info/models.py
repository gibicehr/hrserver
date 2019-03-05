import json

from django.db import models


NAME_MAX_LENGTH = 256


class Staff(models.Model):
    id = models.CharField(max_length=8, primary_key=True)
    first_name = models.CharField(max_length=NAME_MAX_LENGTH)
    last_name = models.CharField(max_length=NAME_MAX_LENGTH)
    email = models.EmailField()

    def to_dict(self):
        dict_ = {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
        }
        return dict_

    def to_json(self):
        dict_ = self.to_dict()
        json_string = json.dumps(dict_)
        return json_string

