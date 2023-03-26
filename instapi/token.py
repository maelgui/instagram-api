def save_token(token):
    with open("token.txt", "w") as f:
        f.write(token)

def load_token():
    with open("token.txt", "r") as f:
        token = f.readline()
    return token
