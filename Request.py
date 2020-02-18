import requests
un = "username"
pw = "password"
headers = {"content-type": "application/json"}
payload = {"operationName":"users_logUserInEmail","variables":{"audience":"d.joinhoney.com","email":un,"password":pw}}
Sess = requests.post(f"https://d.joinhoney.com/v3", json=payload,headers=headers)

if "errors" in Sess.text:
    print("Invalid Account")
else:
    print("Valid Account")

