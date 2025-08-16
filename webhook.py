import requests

webhook_url_test = "http://localhost:5678/webhook-test/my-webhook"
webhook_url = "http://localhost:5678/webhook/my-webhook"

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