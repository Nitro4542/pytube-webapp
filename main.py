"""A web-based front end for pytube"""
# Import dependencies
from flask import Flask, render_template, request, send_file
from downloader import Downloader

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def start_page():
    """Main page"""
    if request.method == 'POST':
        # Get form data from HTMl file
        url = request.form.get('video_url')
        dl_format = request.form.get('btnradio')
        # Set download path
        dl_path = 'download'

        # Check how the video will be downloaded
        if dl_format == "video":
            # Create a Downloader object and set download folder
            dl = Downloader(url, dl_path)
            dl.download_video()
            # Send downloaded video to the client
            return send_file(dl.full_path('mp4'), as_attachment=True)
        elif dl_format == "audio":
            # Create a Downloader object and set download folder
            dl = Downloader(url, dl_path)
            dl.download_audio()
            # Send downloaded video to the client
            return send_file(dl.full_path('webm'), as_attachment=True)

    # Display the main page
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
