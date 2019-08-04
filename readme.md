# Aio HTTP

**runs on python3**

*dependencies*
python3
subprocess
pip3

no installations needs currently other than python3 for now

```
python3 init.py #runs on port 8080
```

routes
All returns json output
    1. get / *gets all connections*
    2. get /connections *gets all connections*
    3. post /connections *no db currently just saves it on array so refreshes each time server restarts*
    4. get /check/:host *checks ping status with host alone uses nc module instead of ping so we can use port*
    5. gets - /check/:host/port/:port_number *to check with port*


    