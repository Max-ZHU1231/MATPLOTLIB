from random import choice

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self,num_points = 5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        #start point
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""
        while len(self.x_values) < self.num_points:
            x_direction = choice([1,-1])
            x_distance = choice([0,1])
            x_step = x_distance * x_direction

            y_direction = choice([1,-1])
            y_distance = choice([0,1])
            y_step = y_distance * y_direction

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)



