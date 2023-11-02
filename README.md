<div align="center">
    <img src="static/pytube-webapp.png" width="192" height="192" style="display: block; margin: 0 auto"/>
    <h1>pytube-webapp</h1>
    <p>A web-based front end for pytube</p>
</div>

---

<p align="center">
    <img src="branding/screenshot.png">
</p>

## Features

- Download YouTube videos as MP4 or as WEBM

## Installation / Setup

First install all requirements from requirements.txt:

```bash
pip install -r requirements.txt
```

After you have installed Flask, make sure to disable debug mode!  
This step is crucial!
Make sure to change the following lines in [main.py](main.py) from this:

```python
if __name__ == "__main__":
    app.run(debug=True)
```

...to this:  

```python
if __name__ == "__main__":
    app.run()
```

To start the website, run [main.py](main.py) like this:

```bash
python main.py
```

### Google Colab

Copy [this file](pytube-webapp-colab.ipynb) to your Google Drive and follow the instructions.

Set the instance type to CPU for the best performance.

## How to use it

First, insert any URL from YouTube into the URL bar.  
  
Next, select your preferred format and click "Download"
