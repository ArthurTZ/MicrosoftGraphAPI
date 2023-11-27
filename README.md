# MicrosoftGraphAPI
### Using Python to consume Microsoft Graph API to create webhook from outlook Email.
### This project integrates with the Microsoft Graph API to manage webhooks, receive notifications, and interact with Microsoft 365 emails.
### I n this project, we're creating a API to receive user informations within a outlook folder
## Environment Setup
### 1. Virtual Environment Setup (Optional but recommended)
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Azure Configuration and APP Registration:
    Create an account on the Azure Portal.
    Go to "Azure Active Directory" > "App registrations" > "New registration."
    After creating the application, note the Application (client) ID and Directory (tenant) ID.
    Create a client secret and note the generated value.

### 4. Enviroment Configuration:
Create a '.env' file in the project root with following information:
``` bash
AZURE_CLIENT_ID=your_client_id
AZURE_TENANT_ID=your_tenant_id
AZURE_CLIENT_SECRET=your_client_secret
```

### 5. Local API configuration:
Use Flask and ngrok to test all methods after deploying it!:
### First to create a webhook, you need a route to receive its information
### note the : after you create a webhook, the route needs to be "online" and the route also needs to respond with a 200 OK with the validationToken
### Creating a route:
```
Flask-Route:
app.route("/webhook", methods=["GET", "POST"])
def webhook():
if request.method == 'POST'
  validationToken = request.args.get('validationToken')
  if validationToken : return Response(validationToken, status=200, mimetype='text/plain')
```

Microsoft demands the user to get the access_token to use its methods:
```bash
First_one : get the User_token 
Check : python src/get_token.py
```

### 6. Webhook:
```
Webhook code : python scr/webhook.py
```

## For more information about the API : https://docs.microsoft.com/en-us/graph/overview






