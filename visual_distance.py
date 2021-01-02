import numpy as np

class visualAngle:
    def __init__(self):
        self.height = float(input("Target's height (in meter):\n"))
        self.distance = float(input("Simulated distance (in meter) between the observer and the target:\n"))
        self.screen_d = float(input("Distance (in meter) between the observer and the screen:\n"))
        self.resolution_length = float(input("Resolution of the screen (length):\n"))
        self.resolution_width = float(input("Resolution of the screen (width):\n"))
        self.screen_size = float(input("Size of the screen (inch):\n"))
    
    def calc_angle(self):
        return 2 * np.arctan(self.height / (2 * self.distance))

    def calc_height_on_screen(self):
        return 2 * self.screen_d * np.tan(self.calc_angle() / 2)

    def calc_ppi(self):
        # return np.sqrt(self.resolution_length ** 2 + self.resolution_width ** 2) / self.screen_size
        return np.sqrt(self.resolution_length ** 2 + self.resolution_width ** 2) / self.screen_size

    def calc_resolution_on_screen(self):
        return (self.calc_height_on_screen() / 0.0254) * self.calc_ppi()

def main():

    Continue = True
    while Continue:
        v = visualAngle()
        h = v.calc_height_on_screen()
        ppi = v.calc_ppi()
        r = v.calc_resolution_on_screen()
        print("The image is %f-meter-high on the screen." % (h))
        print("The PPI of your screen is %f." % (ppi))
        print("The resolution of the image on screen (height) is %f." % (r))

        if input("Continue? y/n\n") == "n":
            Continue = False

main()