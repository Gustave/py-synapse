# Py-Synapse
A simple Python wrapper for [hubot-synapse][hubot-synapse] using
[redis-py][redis-py].

## Getting started
```python
# main.py

from synapse import Neuron
import redis

# Connect to Redis
conn = redis.StrictRedis(host='localhost', port=6379, db=0)

# Just pass in the name of your Hubot and a Redis connection
neuron = Neuron("hubot", conn)

# Create a listener function
def echo_listener(neuron, msg):
    neuron.send("speak", msg)

# Register your listener with your neuron
neuron.listen("respond", echo_listener)
```

You can find out more about the different channels that Synapse communicates on
in the [hubot-synapse README][hubot-synapse].

[hubot-synapse]: http://github.com/Gustave/hubot-synapse
[redis-py]: https://github.com/andymccurdy/redis-py
