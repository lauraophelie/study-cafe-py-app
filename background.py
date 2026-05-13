import csv

class Map:
    def __init__(self, csv_file, tile_images, tile_size=32):
        self.tile_size = tile_size
        self.tile_images = tile_images
        self.tile_map = []
        self.load_csv(csv_file)

    def load_csv(self, csv_file):
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.tile_map.append([int(tile) for tile in row])

    def render(self, window, position_x = 0, position_y = 0):
        start_col = max(0, position_x // self.tile_size)
        end_col = min(len(self.tile_map[0]), (position_x + window.get_width()) // self.tile_size + 2)

        start_row = max(0, position_y // self.tile_size)
        end_row = min(len(self.tile_map), (position_y + window.get_height()) // self.tile_size + 2)

        for row in range(start_row, end_row):
            for col in range(start_col, end_col):
                tile_index = self.tile_map[row][col]
                if tile_index >= 0:
                    x = col * self.tile_size - position_x
                    y = row * self.tile_size - position_y
                    window.blit(self.tile_images[tile_index], (x, y))