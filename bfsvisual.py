import turtle
import time
from collections import deque

turtle.hideturtle()
# Graph structure (edge list)   
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}

# Coordinates for drawing nodes
positions = {
    'A': (-50, 100),
    'B': (-150, 50),
    'C': (50, 50),
    'D': (-200, 0),
    'E': (-100, 0),
    'F': (0, 0),
    'G': (100, 0)
}
turtle.speed("fastest")


# Draw edges
def draw_edges(pen, graph, positions):
    pen.color("black")
    for node in graph:
        for neighbor in graph[node]:
            x1, y1 = positions[node]
            x2, y2 = positions[neighbor]
            pen.penup()
            pen.goto(x1, y1)
            pen.pendown()
            pen.goto(x2, y2)

# Draw nodes
def draw_node(pen, label, position, color="white"):
    x, y = position
    pen.penup()
    pen.goto(x, y - 20)
    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(20)
    pen.end_fill()
    pen.goto(x, y - 5)
    pen.color("white")
    pen.write(label, align="center", font=("Arial", 12, "bold"))

# BFS traversal and visualization
def bfs_turtle(graph, start, positions):
    visited = set()
    queue = deque([start])
    order = []
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            order.append(node)
            draw_node(pen, node, positions[node], color="lightgreen")
            for neighbor in graph[node]:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)

# Set up turtle window
screen = turtle.Screen()
screen.title("BFS Visualization with Turtle")

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

# Draw the static graph first
draw_edges(pen, graph, positions)
for node in graph:
    draw_node(pen, node, positions[node], color="lightblue")

# Run BFS traversal with visualization
pen.speed(1)
bfs_turtle(graph, 'A', positions)

turtle.done()
