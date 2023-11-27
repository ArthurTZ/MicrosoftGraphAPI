from msal import ConfidentialClientApplication

scopes = ['https://graph.microsoft.com/.default']

def _getToken():
    """
    Acquires an access token for authentication using the `ConfidentialClientApplication` class from the `msal` library.

    Returns:
    - str: The access token obtained for authentication with the Microsoft Graph API.
    """
    instance = ConfidentialClientApplication(
        client_id=AZURE_APP_ID,
        client_credential=AZURE_APP_SECRET,
        authority=f"https://login.microsoftonline.com/{AZURE_APP_TENANT}/"
    )

    token = instance.acquire_token_for_client(scopes=scopes)
    access_token = token['access_token']
    
    if access_token: return access_token
    else: print("Failed to get the token")