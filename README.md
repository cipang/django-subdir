# Deploying Django Applications in a Subdirectory

This README is for a record for research done for this topic.

## Nginx Config
```
location /dir/ {    # Must have trailing slash
        include proxy_params;
        proxy_pass http://127.0.0.1:8002/;  # Must have trailing slash
}
```

## Django Config (settings.py)
```
FORCE_SCRIPT_NAME = "/dir/"
```
Note: This must be identical to the Nginx location

## This Project

This project is for printing out all ``META``, ``GET``
and ``POST`` values in ``request`` for debugging.