# Checks the model, if the data isn't already present, send an sms to the given number


def hello():
    import requests
    url = "https://www.fast2sms.com/dev/bulk"
    payload = "sender_id=FSTSMS&message=Siiii&language=english&route=p&numbers=9962017896"
    headers = {'authorization': "gjnoaMcX65G80yl3zeKxD7PibwrHWBZIVkY9LtJ4dEup2qFsNSpGaFX0yMRsc6HjhPeJzKwNEqCgrBOu",'Content-Type': "application/x-www-form-urlencoded",'Cache-Control': "no-cache",}
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)

hello()

