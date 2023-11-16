from matplotlib import pyplot as plt

class Spline():
    def __init__(self, points: list[tuple[float, float]], show_points: bool = False) -> None:
        self.points = points
        self.show_points = show_points

    def generate(self):
        '''
        Generates the points of the spline
        '''
        self.path: list[tuple[float, float]] = []

        _dt = 1E-8
        _t = 0

        while _t < 1:
            for i in range(len(self.points)):
                print(i)
                # pass

            _t += _dt

    def draw(self):
        '''
        Draws the spline
        '''
        if len(self.path) == 0:
            print("Error: Generate spline before drawing.\n")
            return

        plt.draw()
        plt.show()

def main():
    spline = Spline([(1,1), (3,1), (2,3), (4,2)])
    spline.generate()
    spline.draw()

if __name__ == "__main__":
    main()
