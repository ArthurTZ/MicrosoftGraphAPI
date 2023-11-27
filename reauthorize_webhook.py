import requests
from get_token import _getToken 
from webhook_create import api_url

token = _getToken()

def reauthorize_webhook(subscription_id):
        """
        Reauthorizes the webhook subscription if it needs to be reauthorized.

        Args:
            - subscription_id (str): The ID of the webhook subscription.

        Returns:
            - bool: True if reauthorization is successful, False otherwise.
        """
        headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json",
        }

        subscription_url = f"{api_url}/subscriptions/{subscription_id}/reauthorize"
        response = requests.post(subscription_url, headers=headers)

        if response.status_code:
            return True  # Reauthorization successful
        else:
            return False  # Reauthorization failed