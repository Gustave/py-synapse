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
listener_thread = neuron.listen("respond", echo_listener)
```

The function which you pass to `listen()` is executed in a separate thread
which is then returned to the caller. The `Thread` is already started, so it is
up to you to call `Thread.stop()` later. Unfortunately, the threads are not
currently daemonized due to a shortcoming in [redis-py][redis-py]. You can go
+1 the pull request at andymccurdy/redis-py#640

You can find out more about the different channels that Synapse communicates on
in the [hubot-synapse README][hubot-synapse].

[hubot-synapse]: http://github.com/Gustave/hubot-synapse
[redis-py]: https://github.com/andymccurdy/redis-py
