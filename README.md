# Ray Casting Simulation

This project is a 2D ray casting simulation implemented using Pyglet, demonstrating light behavior in a simple environment.

## Features

- Particles that emit rays in all directions
- Boundaries that reflect rays
- Real-time interaction with mouse movement
- Fullscreen display
- Dynamic boundary creation

## Requirements

- Python 3.x
- Pyglet library

## Installation

1. Clone this repository or download the source code.
2. Install the required dependencies:

```
pip install pyglet
```

## Usage

Run the `space.py` file to start the simulation:

```
python space.py
```

- Move your mouse to change the position of the light source.
- Press the SPACE key to generate new random boundaries.

## Files

- `space.py`: Main file that sets up the window and runs the simulation
- `particles.py`: Defines the Particles class, which represents the light source
- `ray.py`: Implements the Ray class for individual light rays
- `boundary.py`: Contains the Boundary class for creating reflective surfaces

## How It Works

1. The simulation creates a fullscreen window using Pyglet.
2. Particles (light sources) are placed in the center of the screen initially.
3. Rays are cast from the particles in all directions.
4. Boundaries are created randomly in the space.
5. The rays interact with the boundaries, showing reflection and intersection points.
6. Mouse movement updates the position of the particles, recalculating ray interactions in real-time.

## Contributing

Contributions to improve the simulation or add new features are welcome. Please feel free to submit pull requests or open issues for any bugs or enhancements.

## License

This project is open-source and available under the MIT License.