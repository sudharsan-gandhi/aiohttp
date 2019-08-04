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

  

#routes

All returns json output
> get / 
> 
> :gets all connections
> 
> get /connections 
> 
> :gets all connections
> 
> post /connections 
> 
> :no db currently just saves it on array so refreshes each time server restarts
> 
> get /check/:host 
> 
> :checks ping status with host alone uses nc module instead of ping so we can use port
> 
> gets - /check/:host/port/:port_number 
> 
> :to check with port