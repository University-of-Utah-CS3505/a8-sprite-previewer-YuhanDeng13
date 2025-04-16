#a8-sprite-previewer-YuhanDeng13
import math

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

# This function loads a series of sprite images stored in a folder with a
# consistent naming pattern: sprite_# or sprite_##. It returns a list of the images.
def load_sprite(sprite_folder_name, number_of_frames):
    frames = []
    padding = math.ceil(math.log(number_of_frames - 1, 10))
    for frame in range(number_of_frames):
        folder_and_file_name = sprite_folder_name + "/sprite_" + str(frame).rjust(padding, '0') + ".png"
        frames.append(QPixmap(folder_and_file_name))

    return frames

class SpritePreview(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sprite Animation Preview")
        # This loads the provided sprite and would need to be changed for your own.
        self.num_frames = 21
        self.frames = load_sprite('spriteImages',self.num_frames)

        # Add any other instance variables needed to track information as the program
        # runs here
        self.start_value = 30
        self.start_frames = 0
        self.is_playing = False

        # Make the GUI in the setupUI method
        self.setupUI()


    def setupUI(self):
        # An application needs a central widget - often a QFrame
        frame = QFrame()

        main_layout = QVBoxLayout()

        layout1 = QHBoxLayout()

        # Sprite image display
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setFixedSize(150, 150)
        layout1.addWidget(self.image_label)

        self.slider = QSlider(Qt.Orientation.Vertical)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)

        self.slider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.slider.setTickInterval(10)

        layout1.addWidget(self.slider)

        main_layout.addLayout(layout1)

        layout2 = QHBoxLayout()
        self_fps_text = QLabel("Frames per second")
        layout2.addWidget(self_fps_text)

        self_fps_value= QLabel(str(self.start_value))
        layout2.addWidget(self_fps_value)
        main_layout.addLayout(layout2)

        layout3 = QHBoxLayout()

        self.start_bottom = QPushButton("Start")
        layout3.addWidget(self.start_bottom)
        main_layout.addLayout(layout3)


        # Add a lot of code here to make layouts, more QFrame or QWidgets, and
        # the other components of the program.



        # Create needed connections between the UI components and slot methods
        # you define in this class.
        frame.setLayout(main_layout)
        self.setCentralWidget(frame)


    # You will need methods in the class to act as slots to connect to signals

def main():
    app = QApplication([])
    # Create our custom application
    window = SpritePreview()
    # And show it
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
