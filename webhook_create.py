import requests
from get_token import _getToken


api_url = "https://graph.microsoft.com/v1.0"

def _get_webhook(self):
    if token:= _getToken():
        webhook_url = "PUT YOUR URL HERE"
        lifecycle_url = "PUT YOUR lifecycle URL HERE"
        webhook_resource = f"/users/{user_id}/mailFolders('{folder_id}')/messages/"

        headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"
        }

        subscription_data = {
            "changeType": "created",
            "notificationUrl": webhook_url,
            "resource": webhook_resource,
            "expirationDateTime": "2023-11-13T22:30:00-03:00",
            "lifecycleNotificationUrl" : lifecycle_url
        }

        create_webhook = f"{api_url}/subscriptions"
        response = requests.post(create_webhook, headers=headers, json=subscription_data)

        if response.status_code == 201:  
            subscription = response.json()
            print(subscription)
            print(f"Webhook Created, Subscription ID : {subscription['id']}")
        else:
            print(f'Failed to create webhook :  {response.status_code} - {response.text} -')

    else:
        print("Access Token failed")
