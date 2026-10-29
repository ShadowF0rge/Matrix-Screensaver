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

RGB colors use values from `0` to `255`, in the order `(red, green, blue)`.

### Change the Matrix rain colors

Open `settings.py` in your editor. Change `BACKGROUND_COLOR` for the background, `CRIMSON_HEAD_COLOR` for the brightest leading character, and `CRIMSON_TRAIL_COLORS` for the colors of the trailing characters. The variable names still contain `CRIMSON`, but you can use any RGB colors.

For example, replace the existing three color settings with one of these palettes. Keep the rest of `settings.py` unchanged.

#### Crimson Red (default)

```python
BACKGROUND_COLOR = (3, 0, 2)
CRIMSON_HEAD_COLOR = (255, 70, 95)
CRIMSON_TRAIL_COLORS = (
    (235, 20, 55),
    (200, 12, 45),
    (165, 8, 35),
    (125, 5, 27),
    (85, 3, 18),
)
```

#### Matrix Green

```python
BACKGROUND_COLOR = (0, 2, 0)
CRIMSON_HEAD_COLOR = (120, 255, 150)
CRIMSON_TRAIL_COLORS = (
    (50, 255, 100),
    (20, 190, 70),
    (10, 130, 45),
    (5, 80, 25),
    (2, 35, 10),
)
```

#### Cyber Cyan

```python
BACKGROUND_COLOR = (0, 2, 6)
CRIMSON_HEAD_COLOR = (100, 240, 255)
CRIMSON_TRAIL_COLORS = (
    (40, 200, 255),
    (20, 145, 220),
    (10, 95, 170),
    (5, 55, 110),
    (2, 25, 55),
)
```

#### Neon Violet

```python
BACKGROUND_COLOR = (3, 0, 7)
CRIMSON_HEAD_COLOR = (240, 130, 255)
CRIMSON_TRAIL_COLORS = (
    (220, 70, 255),
    (175, 35, 220),
    (130, 15, 175),
    (85, 5, 115),
    (40, 2, 55),
)
```

After changing the values, save `settings.py` and restart the app with `python main.py` for the new colors to take effect.

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

MATRIX TERMINAL is licensed under the MIT License. You are free to use, copy, modify, merge, publish, distribute, sublicense, and sell copies of the software, provided that the original copyright notice and permission notice are included.

See the [`LICENSE`](LICENSE) file for the full license text.

Copyright (c) 2026 Astral Contributors

