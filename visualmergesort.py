import turtle
import random
import time

# Screen setup
screen = turtle.Screen()
screen.title("Merge Sort Visualization")
screen.bgcolor("black")
screen.setup(width=1000, height=600)

# Bar drawer turtle
bar_turtle = turtle.Turtle()
bar_turtle.speed("fastest")  # Set turtle speed to fastest
bar_turtle.hideturtle()
bar_turtle.penup()

# Draw bars from array
def draw_bars(array, color_array):
    bar_turtle.clear()
    x_start = -450
    width = 900 // len(array)
    for i, height in enumerate(array):
        bar_turtle.goto(x_start + i * width, -250)
        bar_turtle.color("white", color_array[i])
        bar_turtle.begin_fill()
        bar_turtle.pendown()
        bar_turtle.forward(width - 1)
        bar_turtle.left(90)
        bar_turtle.forward(height)
        bar_turtle.left(90)
        bar_turtle.forward(width - 1)
        bar_turtle.left(90)
        bar_turtle.forward(height)
        bar_turtle.left(90)
        bar_turtle.penup()
        bar_turtle.end_fill()
    screen.update()

# Merge sort algorithm with visualization
def merge_sort(array, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(array, left, mid)
        merge_sort(array, mid + 1, right)
        merge(array, left, mid, right)
        draw_bars(array, ["green" if left <= x <= right else "white" for x in range(len(array))])

def merge(array, left, mid, right):
    left_part = array[left:mid + 1]
    right_part = array[mid + 1:right + 1]
    i = j = 0
    k = left
    while i < len(left_part) and j < len(right_part):
        if left_part[i] < right_part[j]:
            array[k] = left_part[i]
            i += 1
        else:
            array[k] = right_part[j]
            j += 1
        k += 1
    while i < len(left_part):
        array[k] = left_part[i]
        i += 1
        k += 1
    while j < len(right_part):
        array[k] = right_part[j]
        j += 1
        k += 1



array = [random.randint(20, 300) for _ in range(30)]
draw_bars(array, ["white"] * len(array))
time.sleep(1)
merge_sort(array, 0, len(array) - 1)
draw_bars(array, ["blue"] * len(array))  # Final sorted array

turtle.done()


