from __main__ import app
from flask_marshmallow import Marshmallow

# Init ma
ma = Marshmallow(app)

# Bug Schematics
class BugSchema(ma.Schema):
    class Meta:
        fields = ('report', 'email', 'status', 'id', 'phone', 'created_at')


# Init Schema
bug_schema = BugSchema()
bugs_schema = BugSchema(many=True)