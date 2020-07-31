
map_width, map_height = 900, 600
tile_size = 32
map_grid = []
next_gen = []
number_of_phases = 10

def generate_random_map(array):
    for row_index in range(map_height // tile_size - 1):
        array.append([])
        for cell_index in range(map_width // tile_size - 1):
            if random.randint(0, 2) == 1:
                array[row_index].append(1)
            else:
                array[row_index].append(0)
            if row_index == 0 or cell_index == 0 or row_index == map_height // tile_size or cell_index == map_width // tile_size:
                array[row_index][cell_index] = 1
    return array

def find_amount_of_neighbours(array, row_index, cell_index):
    amount_of_neighbours = 0
    for row_index_offset in range(-1, 2):
        for cell_index_offset in range(-1, 2):
            if row_index == 0 and cell_index == 0:
                continue
            else:
                amount_of_neighbours += array[row_index + row_index_offset][cell_index +cell_index_offset]
    return  amount_of_neighbours

def smooth_phase(array, changing_array, changeing_threshhold):
    for row_index in range(map_height // tile_size - 2):
        for cell_index in range(map_width // tile_size - 2):
            if row_index == 0 or cell_index == 0 or row_index == len(map_grid) or cell_index == len(map_grid[0]):
                changing_array[row_index][cell_index] = array[row_index][cell_index]
                continue
            else:
                amount_of_neighbours = find_amount_of_neighbours(array, row_index, cell_index)
                # print(amount_of_neighbours)
                if amount_of_neighbours == 4:
                    changing_array[row_index][cell_index] = 1
                elif amount_of_neighbours < 4:
                    changing_array[row_index][cell_index] = 0
                elif amount_of_neighbours > 5:
                    changing_array[row_index][cell_index] = 1

    return changing_array

map_grid = generate_random_map(map_grid)
next_gen = map_grid

