import turtle
import math

# Function to draw a colorful spiral
def draw_spiral():
    # Setup Turtle
    turtle.title("Sumesh Graphics On")
    turtle.bgcolor("black")
    turtle.speed(0)  # Fastest drawing speed
    turtle.hideturtle()

    # Define colors
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]

    # Draw spiral
    for i in range(360):
        # Choose color
        turtle.color(colors[i % len(colors)])
        # Move turtle
        turtle.forward(i * 2)
        turtle.left(45)
        
    # Hide turtle and display the result
    turtle.hideturtle()
    turtle.done()

# Main function
def main():
    draw_spiral()

if __name__ == "__main__":
    main()

