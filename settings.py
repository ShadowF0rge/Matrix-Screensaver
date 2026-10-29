"""Visual and runtime settings for MATRIX TERMINAL."""

WINDOW_TITLE = "MATRIX TERMINAL"
DEFAULT_WINDOW_SIZE = (1440, 840)
DEFAULT_FULLSCREEN = False

BACKGROUND_COLOR = (3, 0, 2)
CRIMSON_HEAD_COLOR = (255, 70, 95)

# Trail colors run from brighter red to darker crimson.
CRIMSON_TRAIL_COLORS = (
    (235, 20, 55),
    (200, 12, 45),
    (165, 8, 35),
    (125, 5, 27),
    (85, 3, 18),
)

DEFAULT_FPS = 60
GLYPH_SIZE = 22
MIN_COLUMN_SPACING = 1

# Aqua Kana is preferred if installed; the other names are fallbacks.
FONT_CANDIDATES = (
    "Aqua Kana",
    "Hiragino Sans",
    "Hiragino Kaku Gothic ProN",
    "AppleGothic",
    "Noto Sans CJK JP",
    "Yu Gothic",
)

GLYPHS = (
    "アイウエオカキクケコサシスセソタチツテト"
    "ナニヌネノハヒフヘホマミムメモヤユヨ"
    "ラリルレロワヲン"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "abcdefghijklmnopqrstuvwxyz"
    "0123456789"
    "/<>;:(){}[]&%+-=_!?@#$^*|\\"
)
