import requests

webhook_url_test = "https://n8ntest1416.app.n8n.cloud/webhook-test/my-webhook"
webhook_url = "https://n8ntest1416.app.n8n.cloud/webhook/my-webhook"

def ai_agent(user_input, url=webhook_url):
    if user_input.lower() == "bye":
        return "Thank you for your patience, Bye!"

    data = {
        "chatInput": user_input
    }

    response = requests.post(url, json=data)
    return response.text

if __name__ == "__main__":

    print(ai_agent("Hello"))
