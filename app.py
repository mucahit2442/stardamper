import os
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hakkimizda")
def hakkimizda():
    return render_template("hakkimizda.html")

@app.route("/iletisim")
def iletisim():
    return render_template("iletisim.html")

@app.route("/boya")
def boya():
    resimler = []
    img_folder = os.path.join(app.static_folder, "images")
    for file in sorted(os.listdir(img_folder)):
        if file.startswith("boya") and (file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png")):
            resimler.append("images/" + file)
    return render_template("galeri.html", kategori="Boya, Pasta, Cila", resimler=resimler)

@app.route("/damper")
def damper():
    resimler = []
    img_folder = os.path.join(app.static_folder, "images")
    for file in sorted(os.listdir(img_folder)):
        if file.startswith("damper") and (file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png")):
            resimler.append("images/" + file)
    return render_template("galeri.html", kategori="Damper", resimler=resimler)

@app.route("/pompa")
def pompa():
    resimler = []
    img_folder = os.path.join(app.static_folder, "images")
    for file in sorted(os.listdir(img_folder)):
        if file.startswith("pompa") and (file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png")):
            resimler.append("images/" + file)
    return render_template("galeri.html", kategori="Pompa", resimler=resimler)

@app.route("/boya-videolar")
def boya_videolar():
    videolar = []
    video_folder = os.path.join(app.static_folder, "videos")
    if os.path.exists(video_folder):  # videos klasörü yoksa hata olmasın
        for file in sorted(os.listdir(video_folder)):
            if file.startswith("boya") and file.endswith(".mp4"):
                videolar.append("videos/" + file)
    return render_template("video_galeri.html", kategori="Boya, Pasta, Cila", videolar=videolar)

if __name__ == "__main__":
    app.run(debug=True)
