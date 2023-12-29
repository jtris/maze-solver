# Maze Solver

## Usage
``` cmd
python3 maze_solver.py <path to image>
```

## Showcase

- example image (maze300.png) and the resulting output:

<img src="https://github.com/triskj0/maze-solver/blob/main/mazes/maze300.png" alt="screenshot" width="300"/> <img src="https://github.com/triskj0/maze-solver/blob/main/screenshots/maze300result.png" alt="screenshot" width="300"/>

- example image (maze500.png) and the resulting output:

<img src="https://github.com/triskj0/maze-solver/blob/main/mazes/maze500.png" alt="screenshot" width="300"/> <img src="https://github.com/triskj0/maze-solver/blob/main/screenshots/maze500result.png" alt="screenshot" width="300"/>

## How to run
1. Clone
	```cmd
	git clone https://github.com/triskj0/maze-solver.git

 	cd maze-solver/src
	```

2. Install required packages
	```cmd
	python3 -m pip install -r requirements.txt
	```

3. Run with an example maze
	```cmd
	python3 maze_solver.py ..\mazes\maze300.png
	```

## Using your own mazes
- the mazes it can solve have to follow a certain set of "standards" I've accounted for:

1) it has to be either a **square** or a **rectangle**, doesn't work with round mazes or other unconventional maze shapes

<img src="https://github.com/triskj0/maze-solver/blob/main/screenshots/good_shape.png" alt="good shape example" width="100"/><img src="https://github.com/triskj0/maze-solver/blob/main/screenshots/bad_shape.png" alt="bad shape example" width="100"/>

2) it has to have an **entrance and** an **exit**, i.e. two places where the outer wall is discontinuous (has a hole), right now they can't be on the same side, but I'll add that possibility in the near future

<img src="https://github.com/triskj0/maze-solver/blob/main/screenshots/good_num_openings.png" alt="good number of openings (2)" width="120"/><img src="https://github.com/triskj0/maze-solver/blob/main/screenshots/bad_num_openings.png" alt="bad number of openings" width="120"/><img src="https://github.com/triskj0/maze-solver/blob/main/screenshots/bad_num_openings1.png" alt="bad number of openings" width="120"/>

## About the maze examples in \mazes
- the number always rougly corresponds to the number of pixels if it was a square image
- for example `maze300.png` -> you can assume that the image size is `300x300` px
- maybe you've noticed that `maze400_2.png` doesn't fully obey the maze standards I mentioned before this, yet it still works. That's because when it gets cropped, we're only looking for the top left, bottom right, and then top right corner of the maze, so you might be able to successfully use *some* weird shapes.

<img src="https://github.com/triskj0/maze-solver/blob/main/mazes/maze400_2.png" alt="maze400_2.png" width="220"/>
