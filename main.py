import datetime

from flask import Flask, render_template,url_for

app=Flask(__name__, static_url_path="/static", static_folder="static", template_folder="templates")

class Views:
    class Base:
        @staticmethod
        @app.route("/index")
        def index():
            return f"<h1>Index Page! {datetime.datetime.now()}</h1>"

        @staticmethod
        @app.route("/")
        def home():
            return render_template("home.html")
    class Api:
        @staticmethod
        @app.route("/api")
        def api():
            data= [
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
  },
  {
    "userId": 1,
    "id": 2,
    "title": "qui est esse",
    "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
  },
  {
    "userId": 1,
    "id": 3,
    "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
    "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"
  },]
            return {"status":"OK", "message": data}

    class Books:
        @staticmethod
        @app.route("/ratings/top")
        def ratings_top():
            return f"<h1>top</>"




if __name__== "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)