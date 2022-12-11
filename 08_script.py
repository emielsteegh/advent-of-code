import numpy as np

INPUT_FILE = "in.txt"

def tree_visible_and_scene(grid, x, y):
    if x*y == 0 \
    or x == grid.shape[1]-1 \
    or y == grid.shape[0]-1:
        return True, 0

    height = grid[y, x]

    # find heights of trees up down left and right
    # ? alternatively a single direction + matrix rotations would work, but readability
    u = grid[:y,x][::-1]
    d = grid[y+1:,x]
    l = grid[y,:x][::-1]
    r = grid[y,x+1:]

    # check if height of tree at x,y is bigger than at least one of the maxes
    visibility = height > min([max(h) for h in [u,d,l,r]])
    # scenery score is the product of visible treecount per direction
    # next iterator takes the distance to the first blocking tree
    scenicity = np.prod([next((i+1 for i, tree in enumerate(row) if tree >= height), row.size) for row in [u, d, l, r]])
    
    return visibility, scenicity
        

if __name__ == "__main__":
    with open(INPUT_FILE) as f:
        grid = np.array([[*line[:-1]] for line in f], int)
        vis_grid = grid.copy()
        scene_grid = grid.copy()

        for x in range(grid.shape[1]):
            for y in range(grid.shape[0]):
                vis_grid[y, x], scene_grid[y, x] = tree_visible_and_scene(grid,x,y)
    
        print(f"visibile trees: {vis_grid.sum()} \nmost scenic tree: {scene_grid.max()}")
