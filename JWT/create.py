import jwt
from datetime import datetime, timedelta



secret_key = "" 
 
payload = {
    "username": "rehanraja",
    "exp": datetime.now() + timedelta(days=1)
}

token = jwt.encode(payload, secret_key, algorithm="HS256")
print(token)

decode = jwt.decode(token, secret_key, algorithms="HS256")
print(decode)