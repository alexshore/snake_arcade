import arcade
import numpy as np

SCREEN_SIZE = 400
GRID_SIZE = 20
BLOCK_SIZE = SCREEN_SIZE // GRID_SIZE


class Snake(arcade.Window):
    def __init__(self):
        super(Snake, self).__init__(width=SCREEN_SIZE, height=SCREEN_SIZE, update_rate=1 / 10)
        arcade.set_background_color(arcade.color.SKY_BLUE)

    def setup(self):
        self.current_direction = np.array([1, 0])
        self.length = 1

        self.tiles = np.zeros((GRID_SIZE, GRID_SIZE))
        self.head = [GRID_SIZE // 4, GRID_SIZE // 2]
        self.tiles[*self.head] = self.length
        self.tiles[np.random.randint(0, GRID_SIZE), np.random.randint(0, GRID_SIZE)] = -1

        self.game_over = False
        self.debugging = False

        self.current_score = arcade.Text(
            text="score: 0",
            font_size=24,
            start_x=SCREEN_SIZE // 2,
            start_y=SCREEN_SIZE,
            anchor_x="center",
            anchor_y="top",
        )
        self.current_position = arcade.Text(
            text=f"pos: {self.head}",
            font_size=15,
            start_x=0,
            start_y=SCREEN_SIZE,
            anchor_x="left",
            anchor_y="top",
        )
        self.current_fps = arcade.Text(
            text=f"fps: {arcade.get_fps():.0f}",
            font_size=15,
            start_x=0,
            start_y=SCREEN_SIZE - 20,
            anchor_x="left",
            anchor_y="top",
        )

    def on_key_press(self, symbol: int, modifiers: int):
        match symbol:
            case arcade.key.UP:
                self.current_direction = np.array([0, 1])
            case arcade.key.RIGHT:
                self.current_direction = np.array([1, 0])
            case arcade.key.DOWN:
                self.current_direction = np.array([0, -1])
            case arcade.key.LEFT:
                self.current_direction = np.array([-1, 0])
            case arcade.key.Q:
                self.setup()
            case arcade.key.GRAVE:
                self.debugging = not self.debugging

    def on_draw(self):
        self.clear()
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if self.tiles[i, j] == self.length:
                    arcade.draw_xywh_rectangle_filled(
                        i * BLOCK_SIZE,
                        j * BLOCK_SIZE,
                        BLOCK_SIZE,
                        BLOCK_SIZE,
                        arcade.color.CATALINA_BLUE,
                    )
                elif self.tiles[i, j] > 0:
                    arcade.draw_xywh_rectangle_filled(
                        i * BLOCK_SIZE,
                        j * BLOCK_SIZE,
                        BLOCK_SIZE,
                        BLOCK_SIZE,
                        arcade.color.BLUE_VIOLET,
                    )
                elif self.tiles[i, j] < 0:
                    arcade.draw_xywh_rectangle_filled(
                        i * BLOCK_SIZE,
                        j * BLOCK_SIZE,
                        BLOCK_SIZE,
                        BLOCK_SIZE,
                        arcade.color.CANDY_APPLE_RED,
                    )

        self.current_score.draw()
        if self.debugging:
            self.current_position.draw()
            self.current_fps.draw()

    def on_update(self, delta_time: float):
        if self.game_over:
            return

        self.head += self.current_direction
        if (
            self.head[0] < 0
            or self.head[0] >= GRID_SIZE
            or self.head[1] < 0
            or self.head[1] >= GRID_SIZE
            or self.tiles[*self.head] > 0
        ):
            self.game_over = True
            return

        if self.tiles[*self.head] == -1:
            self.length += 1
            self.tiles[np.random.randint(0, GRID_SIZE), np.random.randint(0, GRID_SIZE)] = -1
        else:
            self.tiles[self.tiles > 0] -= 1

        self.tiles[*self.head] = self.length

        self.current_score.text = f"score: {self.length - 1}"
        self.current_position.text = f"pos: {self.head}"
        self.current_fps.text = f"fps: {arcade.get_fps():.0f}"


def main():
    game = Snake()
    game.setup()
    arcade.enable_timings()
    arcade.run()


if __name__ == "__main__":
    main()
