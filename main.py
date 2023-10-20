import os
from flask import Flask, render_template, request, send_file, redirect
from downloader import Downloader

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def start_page():
    if request.method == 'POST':
        url = request.form.get('video_url')
        dl_format = request.form.get('btnradio')
        dl_path = 'download\\'

        if dl_format == "video":
            dl = Downloader(url, dl_path)
            dl.download_video()
            return send_file(dl.full_path('mp4'), as_attachment=True)
        elif dl_format == "audio":
            dl = Downloader(url, dl_path)
            dl.download_audio()
            return send_file(dl.full_path('webm'), as_attachment=True)

    return render_template('index.html')


@app.route('/download/<file>')
def download_file_to_client(file):
    return send_file(file, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
