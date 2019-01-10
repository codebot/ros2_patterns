# ros2_patterns

Greetings. This isn't a real package, just a few little test programs.

## Add security sauce

#### securing my_service

```
ros2 security create_keystore keys
ros2 security create_key keys test_service
ros2 security create_key keys test_client
```

Terminal 1 for the service:
```
export ROS_SECURITY_ROOT_DIRECTORY=`pwd`/keys
export ROS_SECURITY_ENABLE=true
export ROS_SECURITY_STRATEGY=Enforce
./test_service.py
```

Terminal 2 for the client:
```
export ROS_SECURITY_ROOT_DIRECTORY=`pwd`/keys
export ROS_SECURITY_ENABLE=true
export ROS_SECURITY_STRATEGY=Enforce
./test_client.py
```

Performance will be slower during connect because the `ros2` daemon can't
help (by design), so discovery will actually be encrypted peer-to-peer. Note
that much of the latency of setting up encrypted connections is during the
discovery phase, so this example is basically the most inefficient case
possible: it's a new client that starts, does a single trivial request/reply,
and immediately exits.
