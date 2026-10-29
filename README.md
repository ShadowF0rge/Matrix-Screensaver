# MATRIX TERMINAL

A standalone, screensaver-style Matrix digital-rain app for macOS, built with Python and Pygame. It features a dark background, cinematic crimson-red trails, and a mix of Japanese Katakana, Latin letters, numbers, and programming symbols.

> This is a regular desktop application with a fullscreen mode. It is not a native macOS `.saver` screensaver module.

## Features

- Standalone Pygame window (default: 1440 × 840)
- Optional fullscreen mode
- Crimson-red digital rain on a near-black background
- Mixed character set:
  - Japanese Katakana
  - Uppercase and lowercase Latin letters
  - Numbers
  - Programming and punctuation symbols such as `/<>;:(){}[]&%`
- Animated streams with changing characters and randomized speeds
- Pause, fullscreen toggle, and reset keyboard shortcuts
- Font selection that prefers Aqua Kana when available and falls back to other installed fonts

## Requirements

- macOS
- Python 3.10 or newer recommended
- pip
- Visual Studio Code is optional but recommended

## Setup

### 1. Clone or download the project

If you use Git:

```bash
git clone <YOUR-REPOSITORY-URL>
cd matrix-terminal
```

Or open the project folder you already created in Visual Studio Code.

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

The terminal prompt may show `(.venv)`. If you customized the displayed environment name to `(Matrix)`, that is only a prompt label; the environment directory can still be named `.venv`.

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Run the app

```bash
python main.py
```

## Controls

| Key | Action |
| --- | --- |
| `F` | Toggle fullscreen/windowed mode |
| `Space` | Pause or resume animation |
| `R` | Reset the rain streams |
| `Esc` or `Q` | Quit the app |
| Window close button | Quit the app |

## Font support

The app tries to use these fonts in order:

1. Aqua Kana
2. Hiragino Sans
3. Hiragino Kaku Gothic ProN
4. AppleGothic
5. Noto Sans CJK JP
6. Yu Gothic

The exact font names available depend on your macOS version and installed fonts. If none match, Pygame uses its built-in default font. That fallback may not contain all Japanese characters, so some glyphs may appear as boxes.

### Check Aqua Kana

Open **Font Book** on macOS and search for `Aqua Kana` or `Aqua かな`. If it is installed, the app will attempt to use it. If the Japanese characters do not render correctly, try another installed Japanese-capable font and add its family name to `FONT_CANDIDATES` in `settings.py`.

## Configuration

Edit `settings.py` to adjust:

- `DEFAULT_WINDOW_SIZE`: default window width and height
- `DEFAULT_FULLSCREEN`: start in fullscreen (`True`) or windowed (`False`) mode
- `BACKGROUND_COLOR`: background RGB color
- `CRIMSON_HEAD_COLOR`: brighter color used for the leading character
- `CRIMSON_TRAIL_COLORS`: colors used for the trailing characters
- `DEFAULT_FPS`: target frame rate
- `GLYPH_SIZE`: font size and approximate vertical spacing
- `MIN_COLUMN_SPACING`: horizontal spacing between streams
- `GLYPHS`: characters used by the animation
- `FONT_CANDIDATES`: font families to try

RGB colors use values from `0` to `255`.

## Project structure

```text
matrix-terminal/
├── main.py
├── settings.py
├── requirements.txt
├── README.md
└── .gitignore
```

- `main.py` initializes Pygame, handles events, updates the animation, and draws the streams.
- `settings.py` contains visual settings, font preferences, and the character set.
- `requirements.txt` lists Python dependencies.

## Build a macOS app

You can package the project as an app bundle with PyInstaller. Packaging should be tested on the Mac that will run the app.

Install PyInstaller:

```bash
python -m pip install pyinstaller
```

Build a windowed app:

```bash
python -m PyInstaller --windowed --name "MATRIX TERMINAL" main.py
```

When the build finishes, check the `dist/` folder for the app bundle.

Notes:

- The `.app` bundle is a standalone desktop app, but it is not automatically a system screensaver.
- Fonts available on your Mac may not be present on another Mac.
- For sharing outside your own Mac, signing and notarization may be needed to avoid macOS security warnings.
- If PyInstaller cannot locate a required font, install the font on the target Mac or configure an explicit font file path.

## Troubleshooting

### `ModuleNotFoundError: No module named 'pygame'`

Make sure the virtual environment is active, then run:

```bash
python -m pip install -r requirements.txt
```

### The window opens and closes immediately

Run the app from the terminal:

```bash
python main.py
```

Read the error printed in the terminal. Confirm that `main.py` and `settings.py` are in the same folder.

### Japanese characters appear as boxes

A font without Japanese glyph support is being used. Install or select a Japanese-capable font, then add its family name to `FONT_CANDIDATES` in `settings.py`.

### The animation is too fast or too slow

Change the speed ranges in `main.py`, inside `create_columns()` and `RainColumn.update()`. You can also adjust `DEFAULT_FPS` in `settings.py`.

## Development roadmap

Potential future improvements:

- In-app settings panel
- Configurable speed and density
- Glow effects and fading trails
- Custom app icon
- Save settings between launches
- Optional launch after inactivity
- Native macOS screensaver integration (a separate, more advanced step)

## License

Choose a license before publishing the project publicly. For example, the MIT License is a common permissive option; add a `LICENSE` file if you decide to use it.
