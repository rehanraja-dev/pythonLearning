import jwt
from datetime import datetime, timedelta


secret_key = "lauda" 
 
payload1 = {
    "username": "rehanraja",
    "exp": datetime.now() + timedelta(minutes=300),
    "type": "access"
}

access_token = jwt.encode(payload1, secret_key, algorithm="HS256")
print(access_token)

payload2 = {
    "username": "rehanraja",
    "exp": datetime.now() + timedelta(days=14),
    "type": "refresh"
}

refresh_token = jwt.encode(payload2, secret_key, algorithm="HS256")
print(refresh_token)

decode1 = jwt.decode(access_token, secret_key, algorithms="HS256")
print(decode1)


decode2 = jwt.decode(refresh_token, secret_key, algorithms="HS256")
print(decode2)