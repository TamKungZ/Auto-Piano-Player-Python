# Auto Piano Player v0.0.1

**By TamKungZ_**

## Description

Auto Piano Player is a Python-based tool designed to automate keypress sequences for playing virtual pianos. It allows users to easily configure key presses and delays between them, with additional features like looping, adding multiple keys per sequence, and saving/loading configurations from a JSON file.

## Features

- **Add multiple keys**: Allows you to add multiple keys to be played together.
- **Loop function**: Play key sequences in a loop.
- **JSON save/load**: Save your key configurations and load them when needed.
- **Hotkey support**: Activate the auto-play using `Ctrl+Shift+P`.
- **Clear all keys**: Easily clear all added keys with one click.
- **On-screen control**: Simple, user-friendly interface with buttons to start, stop, add keys, and toggle looping.

## Requirements

- Python 3.x
- Libraries:
  - tkinter
  - pynput
  - keyboard

## Installation

1. Clone or download this repository.
2. Install the required Python libraries:
    ```
    pip install pynput keyboard
    ```
3. Run the application:
    ```
    python AutoPianoPlayer.py
    ```

## Usage

1. Use the "Add Key" button to add keypresses and delays.
2. Configure the play settings, including loop mode.
3. Press "Play Auto" to start the automatic keypress sequence, and "Stop" to halt it.
4. Use the "Save" and "Load" buttons to save your settings in a JSON file.
5. Use "Clear" to reset all key entries.
