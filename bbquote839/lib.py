import requests

def get_quote():

    response = requests.get("https://wagon-breaking-bad-quotes.herokuapp.com/v1/quotes").json()[0]
    return f"Quote : {response['quote']} \n>Auteur : {response['author']}"

if __name__ == "__main__":
    print(get_quote())
