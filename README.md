# Python Media Player

A lightweight and modern **media player** built with Python. This application allows users to play, pause, and manage their audio and video files with a clean graphical user interface.

## Features

- **Audio & Video Playback:** Supports MP3, WAV, MP4, MKV, and more.
- **Playlist Management:** Create, save, and load custom playlists.
- **Modern UI:** Clean and intuitive interface built with custom styling.
- **Controls:** Play, pause, stop, skip, volume control, and progress tracking.

## Installation

### Prerequisites

Make sure you have **Python 3.8+** installed on your system.

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd media-player
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To start the media player, run the main script from your terminal:

```bash
python main.py
```

## Technologies Used

- **Python 3** - Core programming language.
- **Tkinter / PyQt6** - Graphical User Interface (GUI) framework.
- **Pygame / VLC-Python** - Media playback engine.

## License

This project is licensed under the **MIT License** - see the LICENSE file for details.
