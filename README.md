# Pygame 3D Visualization

This Python script uses the Pygame library to create a simple 3D visualization of circles and edges. The script defines classes for managing shapes, their positions, and their transformations. It also includes a basic user interface to interact with the visualization by rotating and transforming the shapes.

## Features

- 3D transformations: Rotate and transform shapes in 3D space.
- User Interface: Use keyboard events to interact with the 3D scene.
- Circle Distance and Edge Creation: Find distances between circles and create edges between the closest circles.
- Continuous Execution: The script runs in an infinite loop to continuously update the display based on user interactions.

## Getting Started

1. **Install Dependencies:**
   - Make sure you have Python installed on your machine.
   - Install the Pygame library using the following command:
     ```bash
     pip install pygame
     ```

2. **Run the Script:**
   - Execute the script using the following command:
     ```bash
     python your_script_name.py
     ```
     Replace `your_script_name.py` with the name of your Python script.

3. **Interact with the Visualization:**
   - Use the following keys to interact with the 3D scene:
     - W/S: Rotate around the X-axis.
     - A/D: Rotate around the Y-axis.
     - Q/E: Rotate around the Z-axis.
     - Arrow keys: Transform along the X and Y axes.

## Code Structure

- `Position`: Class representing a 3D position.
- `ShapeObject`: Class managing lists of shapes (circles and edges).
- `Shape`: Abstract class for defining shapes and their transformations.
- `Edge`: Class representing an edge connecting two positions.
- `Circle`: Class representing a circle in 3D space.
- `ShapeManagement`: Class managing the drawing and transformation of shapes.
- `FindDistance`: Class for finding distances between circles.
- `WindowManagement`: Class handling user input and triggering corresponding actions.

## Contributing

If you have suggestions or find issues with the code, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
