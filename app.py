from flaskapp import app
import os


print(os.getenv("APP_SETTINGS"))
@app.route("/")
def home():
    return "<h1>Hello World</h1>"

@app.route("/<name>")
def home_user(name):
    return f"<h1>Hello {name}</h1>"

if __name__ == "__main__":
    app.debug = True
    app.run()
