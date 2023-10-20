from pytube import YouTube


class Downloader:
    def __init__(self, url, dl_path):
        self.url = url
        self.dl_path = dl_path
        self.stream = None

    def download_video(self):
        video = YouTube(self.url)
        self.stream = video.streams.get_highest_resolution()
        self.stream.download(self.dl_path)

    def download_audio(self):
        video = YouTube(self.url)
        self.stream = video.streams.get_by_itag(251)
        self.stream.download(self.dl_path)

    def full_path(self, file_format):
        full_path = self.dl_path + self.stream.title + '.' + file_format
        return full_path
