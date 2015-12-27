import micromodels
import json
import datetime
__author__ = 'Daniel'


class ExampleModel(micromodels.Model):
    myfield = micromodels.CharField()
    time = micromodels.DateTimeField()

e = ExampleModel.from_dict(json.dumps({'myfield': 'Some Value', 'time': '2012-05-29T19:30:03.000283+00:00'}), is_json=True)
print e.to_json()
e.myfield = "a"
e.time = datetime.datetime.now()
print e.to_json()
print e.to_dict()