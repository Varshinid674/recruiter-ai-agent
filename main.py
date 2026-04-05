from fastapi import FastAPI

app = FastAPI()

users = {
    "admin": "1234",
    "recruiter": "abcd"
}

@app.get("/")
def home():
    return {"message": "Backend Running"}

@app.get("/login")
def login(username: str, password: str):
    if username in users and users[username] == password:
        return {"status": "Login successful"}
    return {"status": "Invalid login"}