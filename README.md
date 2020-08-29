# youtube-dl-wrapper

This small repo will automatically download YouTube videos (using youtube-dl), convert them to mp3 files and attempt to populate the metadata such that the songs are more presentable for DJing software (by correctly setting the `Title` and `Artist` fields).

# Installation

Brace yourself Skews..

## 1. Install Anaconda

Download Anaconda Individual Edition from https://www.anaconda.com/products/individual and run the installer.

## 2. Install FFmpeg

Visit https://ffmpeg.org/download.html and follow the links to download the build for your operating system:
- Windows: https://ffmpeg.zeranoe.com/builds/
- Mac: https://evermeet.cx/ffmpeg/
- Linux:
    - Debian: https://tracker.debian.org/pkg/ffmpeg
    - Ubuntu: https://launchpad.net/ubuntu/+source/ffmpeg
    - Fedora and Red Hat: https://rpmfusion.org/

### Windows Installation:

- Extract the downloaded zip file e.g. into `C:/Program Files/`.
- Rename the folder to `ffmpeg`.
- Add `ffmpeg/bin` to `PATH`:
    - Search for environment variables in the Windows search bar and press `Enter`.
    - This will open a window titled `System Properties`.
    - Click on the `Environment Variables...` button near the bottom of the window.
    - In the `System Variables` list, scroll down to the Variable called `Path`.
    - Select `Path` and click `Edit...`.
    - On the right hand side of the window press `Browse...` and navigate to the `ffmpeg` folder that you extracted earlier.
    - Single click on `ffmpeg/bin` (`bin` for binaries, basically the actual executable files that will convert the video to audio. The Python interpreter will look for `ffmpeg/bin` in the `Path` to be able to carry out the conversion.)
    - Keep pressing `Okay` on each window until all windows are closed.

# Usage

### 1. Open the Anaconda Prompt (Anaconda Powershell Prompt on Windows)

### 2. Navigate to this project directory

e.g. `cd C:\Users\Shared\Documents\Projects\youtube-dl-wrapper`

### 3. Create the Conda environment

`conda env create -f environment.yml`

### 4. Activate the Conda environment

`conda activate youtube-dl-wrapper`

### 5. Run the script

`python download_songs.py --url https://youtube.com/watch?...`

The YouTube link can either be a playlist or single video.
It is recommended that once a batch of songs have been downloaded and converted that they are removed from the `downloaded_songs` directory.