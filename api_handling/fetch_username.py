import requests

def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()
    if data["success"] and "data" in data:
        res = data["data"]['name']['first']
        print(res)

def main():
    fetch_random_user()

if __name__ == "__main__":
    main()