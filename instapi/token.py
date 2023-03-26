def save_token(token):
    with open("data/token.txt", "w") as f:
        f.write(token)

def load_token():
    with open("data/token.txt", "r") as f:
        token = f.readline()
    return token
