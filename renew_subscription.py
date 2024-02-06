    

def renew_subscription(self, subscription_id):
        """
        Renews the webhook subscription if it needs to be renewed.

        Args:
            - subscription_id (str): The ID of the webhook subscription.

        Returns:
            - bool: True if the subscription was successfully renewed, False otherwise.

        Raises:
            - Exception: If there is an error in the renewal process.
        """

        expiration_datetime = (dt.utcnow() + timedelta(days=3)).replace(microsecond=0).isoformat() + "Z"
        headers = {
            "Authorization": "Bearer " + self._token,
            "Content-Type": "application/json",
        }
        payload = {
            "expirationDateTime": expiration_datetime
        }
        subscription_url = f"{self.api_url}/subscriptions/{subscription_id}"
        response = requests.patch(subscription_url, headers=headers, json=payload)

        if response.status_code == 200:
            return True  # Subscription renewed successfully
        else:
            raise Exception(f"Erro ao renovar a assinatura do webhook: {response.status_code} - {response.text}")
        
