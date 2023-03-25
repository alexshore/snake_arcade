import arcade
import numpy as np


class Snake(arcade.Window):
    def __init__(self):
        super(Snake, self).__init__(width=600, height=600)
        arcade.set_background_color(arcade.color.MOSS_GREEN)
        self.tiles = np.zeros((30, 30))
        self.head = np.array([14, 14])

    def on_draw(self):
        self.clear()

        for i in range(30):
            for j in range(30):
                if self.tiles[i][j] > 0:
                    color = arcade.color.BLUE_VIOLET
                elif self.tiles[i][j] < 0:
                    color = arcade.color.MOSS_GREEN
                else:
                    color = arcade.color.CANDY_APPLE_RED
                arcade.draw_xywh_rectangle_filled(i * 20, j * 20, 20, 20, color)

    def on_update(self, delta_time: float):
        ...


def main():
    game = Snake()
    arcade.run()


if __name__ == "__main__":
    main()
