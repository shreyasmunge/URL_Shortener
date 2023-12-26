from flask import Flask, render_template, redirect, request
import string
import random

app = Flask(__name__)
url_map={}

def generate_short_url():
    chars=string.ascii_letters+string.digits
    short_url="".join(random.choice(chars) for _ in range(6))
    return short_url

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        long_url=request.form['long_url']
        short_url=generate_short_url()
        while short_url in url_map:
            short_url=generate_short_url()
        url_map[short_url]=long_url
        return f"shortened url: {request.url_root}{short_url}"
    return render_template("index.html")


@app.route("/<short_url>")
def redirect_url(short_url):
    long_url=url_map[short_url]
    if long_url:
        return redirect(long_url)
    else:
        return "url not found",404
    

if __name__=="__main__":
    app.run(debug=True)