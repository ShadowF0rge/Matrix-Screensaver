
import random
import pygame

from settings import (
    WINDOW_TITLE,
    DEFAULT_WINDOW_SIZE,
    DEFAULT_FULLSCREEN,
    BACKGROUND_COLOR,
    CRIMSON_HEAD_COLOR,
    CRIMSON_TRAIL_COLORS,
    DEFAULT_FPS,
    GLYPH_SIZE,
    MIN_COLUMN_SPACING,
    FONT_CANDIDATES,
    GLYPHS,
)


def load_font(size: int) -> pygame.font.Font:
    """Load a preferred font, falling back to the default font."""
    available_fonts = pygame.font.get_fonts()

    for candidate in FONT_CANDIDATES:
        font_name = candidate.lower().replace(" ", "").replace("-", "")

        for available in available_fonts:
            normalized = available.lower().replace(" ", "").replace("-", "")

            if font_name == normalized:
                try:
                    return pygame.font.SysFont(candidate, size)
                except pygame.error:
                    continue

    return pygame.font.Font(None, size)


class RainColumn:
    """One vertical stream of falling Matrix characters."""

    def __init__(self, x: int, y: float, speed: float, length: int):
        self.x = x
        self.y = y
        self.speed = speed
        self.length = length
        self.glyphs = [random.choice(GLYPHS) for _ in range(length)]
        self.change_timer = 0.0

    def update(self, dt: float, screen_height: int) -> None:
        self.y += self.speed * dt
        self.change_timer += dt

        if self.change_timer >= 0.09:
            self.change_timer = 0.0

            if self.glyphs:
                index = random.randrange(len(self.glyphs))
                self.glyphs[index] = random.choice(GLYPHS)

        if self.y - self.length * GLYPH_SIZE > screen_height:
            self.y = random.uniform(-screen_height * 0.8, -GLYPH_SIZE)
            self.speed = random.uniform(500.0, 550.0)
            self.length = random.randint(15, 40)
            self.glyphs = [random.choice(GLYPHS) for _ in range(self.length)]


def create_columns(width: int, height: int) -> list[RainColumn]:
    columns = []
    spacing = max(MIN_COLUMN_SPACING, GLYPH_SIZE + 4)

    for x in range(0, width + spacing, spacing):
        columns.append(
            RainColumn(
                x=x,
                y=random.uniform(-height, height),
                speed=random.uniform(100.0, 330.0),
                length=random.randint(15, 40),
            )
        )

    return columns


def draw_column(
    screen: pygame.Surface,
    font: pygame.font.Font,
    column: RainColumn,
) -> None:
    for index, glyph in enumerate(column.glyphs):
        y = int(column.y - index * GLYPH_SIZE)

        if y < -GLYPH_SIZE or y > screen.get_height():
            continue

        if index == 0:
            color = CRIMSON_HEAD_COLOR
        else:
            trail_index = min(
                len(CRIMSON_TRAIL_COLORS) - 1,
                int(
                    index
                    / max(1, column.length)
                    * len(CRIMSON_TRAIL_COLORS)
                ),
            )
            color = CRIMSON_TRAIL_COLORS[trail_index]

        glyph_surface = font.render(glyph, True, color)
        screen.blit(glyph_surface, (column.x, y))


def main() -> None:
    pygame.init()
    pygame.display.set_caption(WINDOW_TITLE)

    if DEFAULT_FULLSCREEN:
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode(
            DEFAULT_WINDOW_SIZE,
            pygame.RESIZABLE,
        )

    clock = pygame.time.Clock()
    font = load_font(GLYPH_SIZE)
    columns = create_columns(screen.get_width(), screen.get_height())

    running = True
    paused = False
    fullscreen = DEFAULT_FULLSCREEN

    while running:
        dt = min(clock.tick(DEFAULT_FPS) / 1000.0, 0.05)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_ESCAPE, pygame.K_q):
                    running = False

                elif event.key == pygame.K_SPACE:
                    paused = not paused

                elif event.key == pygame.K_f:
                    fullscreen = not fullscreen

                    if fullscreen:
                        screen = pygame.display.set_mode(
                            (0, 0),
                            pygame.FULLSCREEN,
                        )
                    else:
                        screen = pygame.display.set_mode(
                            DEFAULT_WINDOW_SIZE,
                            pygame.RESIZABLE,
                        )

                    columns = create_columns(
                        screen.get_width(),
                        screen.get_height(),
                    )

                elif event.key == pygame.K_r:
                    columns = create_columns(
                        screen.get_width(),
                        screen.get_height(),
                    )

            elif event.type == pygame.VIDEORESIZE and not fullscreen:
                screen = pygame.display.set_mode(
                    event.size,
                    pygame.RESIZABLE,
                )
                columns = create_columns(
                    screen.get_width(),
                    screen.get_height(),
                )

        screen.fill(BACKGROUND_COLOR)

        if not paused:
            for column in columns:
                column.update(dt, screen.get_height())
                draw_column(screen, font, column)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
