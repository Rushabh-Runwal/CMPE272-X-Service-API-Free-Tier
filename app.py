from flask import Flask, render_template, request, redirect, url_for, flash
import twitter_service
import logging

app = Flask(__name__)
app.secret_key = "app_secret_key"

logging.basicConfig(level=logging.INFO)
app.logger.addHandler(logging.StreamHandler())

response = twitter_service.get_user_details()

@app.route("/")
def index():
    # flash(response, "details")
    return render_template("index.html")


@app.route("/create_tweet", methods=["POST"])
def create_tweet():
    tweet_content = request.form.get("tweet_content")
    result = twitter_service.create_tweet(tweet_content)
    flash(result, "create")
    return redirect(url_for("index"))


@app.route("/delete_tweet", methods=["POST"])
def delete_tweet():
    tweet_id = request.form.get("tweet_id")
    result = twitter_service.delete_tweet(tweet_id)
    flash(result, "delete")
    return redirect(url_for("index"))

@app.route("/get_user_by_username", methods=["GET"])
def get_user_by_username():
    username = request.form.get("username")
    # result = twitter_service.get_user_by_username(username)
    flash(response, "user_details")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
