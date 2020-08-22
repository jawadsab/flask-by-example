from flaskapp import app

@app.route("/")
def home():
    return "<h1>Hello World</h1>"

if __name__ == "__main__":
    app.debug = True
    app.run()
