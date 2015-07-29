import collections
import json

Message = collections.namedtuple("Message", ["user", "room", "message"])

def serialize_msg(msg):
    try:
        return json.dumps(msg.__dict__)
    except AttributeError:
        return None

def deserialize_msg(msg):
    j = json.loads(msg)
    try:
        return Message(**j)
    except TypeError:
        return None

class Neuron(object):
    def __init__(self, name, conn):
        self._name = name
        self._conn = conn

    def listen(self, event, func):
        def subscriber(redis_msg):
            msg = deserialize_msg(redis_msg['data'])
            if msg is not None:
                func(self, msg)
            
        sub = self._conn.pubsub()
        sub.subscribe(**{"{0}:in:{1}".format(self._name, event): subscriber})
        thread = sub.run_in_thread(sleep_time=0.001)
        return thread

    def send(self, action, message):
        json_msg = serialize_msg(message)
        self._conn.publish("{0}:out:{1}".format(self._name, action), json_msg)
