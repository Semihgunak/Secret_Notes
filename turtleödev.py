import turtle
import random
import time


class TurtleGame:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Kaplumbağa Kaçma Oyunu")
        self.screen.bgcolor("white")
        self.screen.setup(width=800, height=800)

        self.score = 0
        self.score_display = turtle.Turtle()
        self.score_display.penup()
        self.score_display.goto(0, 320)
        self.update_score_display()
        self.remaining_time = 15
        self.score_display.hideturtle()

        self.timer_display = turtle.Turtle()
        self.timer_display.penup()
        self.timer_display.goto(0, 350)
        self.timer_display.hideturtle()


        self.turtle = turtle.Turtle()
        self.turtle.shape("turtle")
        self.turtle.color("green")
        self.turtle.speed(0)
        self.turtle.penup()

        self.start_time = time.time()
        self.move_turtle()

        self.screen.onclick(self.on_click)
        self.update_timer()
    def update_score_display(self):
        self.score_display.clear()
        self.score_display.write(f"Skor: {self.score}", align="center", font=("Courier", 16, "normal"))

    def update_timer_display(self):
        self.timer_display.clear()
        self.timer_display.write(f"Zaman:{self.remaining_time}",move=False, align="center", font=("Courier", 16, "normal"))

    def update_timer(self):
        elapsed_time = int(time.time() - self.start_time)
        self.remaining_time = max(15-elapsed_time, 0)
        self.update_timer_display()

        if self.remaining_time > 0:
            self.screen.ontimer(self.update_timer, 1000)
        else:
            self.timer_display.clear()
            self.screen.onclick(None)

    def move_turtle(self):
        x = random.randint(-190, 190)
        y = random.randint(-190, 190)
        self.turtle.goto(x, y)

        self.move_randomly()

        elapsed_time = int(time.time() - self.start_time)
        if elapsed_time < 15:
            self.screen.ontimer(self.move_turtle, 1000)

    def move_randomly(self):
        angle = random.randint(0, 360)
        distance = random.randint(50, 150)
        self.turtle.setheading(angle)
        self.turtle.forward(distance)

    def on_click(self, x, y):
        turtle_x, turtle_y = self.turtle.pos()
        if turtle_x - 20 <= x <= turtle_x + 20 and turtle_y - 20 <= y <= turtle_y + 20:
            self.score += 1
            self.update_score_display()



if __name__ == "__main__":
    turtle_game = TurtleGame()
    turtle.done()

