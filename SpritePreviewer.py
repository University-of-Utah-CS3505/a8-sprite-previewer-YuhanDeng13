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
        self.setWindowTitle("Sprite Preview")
        # This loads the provided sprite and would need to be changed for your own.
        self.num_frames = 21
        self.frames = load_sprite('spriteImages',self.num_frames)

        # Add any other instance variables needed to track information as the program
        # runs here
        self.value = 25
        self.start_frames = 0
        self.is_playing = False

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)

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

        # Add a lot of code here to make layouts, more QFrame or QWidgets, and
        # the other components of the program.

        self.slider = QSlider(Qt.Orientation.Vertical)
        self.slider.setMinimum(1)
        self.slider.setMaximum(100)
        self.slider.setValue(self.value)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.slider.setTickInterval(10)

        layout1.addWidget(self.slider)

        main_layout.addLayout(layout1)

        layout2 = QHBoxLayout()
        self_fps_text = QLabel("Frames per second")
        layout2.addWidget(self_fps_text)

        self.fps_value= QLabel(str(self.value))
        layout2.addWidget(self.fps_value)
        main_layout.addLayout(layout2)

        layout3 = QHBoxLayout()

        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.toggle_animation)
        layout3.addWidget(self.start_button)
        main_layout.addLayout(layout3)

        # Create needed connections between the UI components and slot methods
        # you define in this class.
        frame.setLayout(main_layout)
        self.setCentralWidget(frame)

        #menu
        menu = self.menuBar()
        file_menu = menu.addMenu("File")

        pause_action = QAction("Pause", self)
        pause_action.triggered.connect(self.toggle_animation)
        file_menu.addAction(pause_action)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)



# You will need methods in the class to act as slots to connect to signals

    def update_fps_value(self):
        self.value = self.slider.value()
        self.fps_value.setText(str(self.value))
        if self.is_playing:
            self.timer.start(int(1000 / self.value))


    def toggle_animation(self):
        if self.is_playing:
            self.stop()
        else:
            self.start()

    def start(self):
        self.is_playing = True
        self.start_button.setText("Stop")
        self.timer.start(int(1000 / self.value))

    def stop(self):
        self.is_playing = False
        self.start_button.setText("Start")
        self.timer.stop()

    def pause_animation(self):
        if self.is_playing:
            self.stop()

    def update_frame(self):
        self.start_frames = (self.start_frames + 1) % self.num_frames
        self.image_label.setPixmap(self.frames[self.start_frames])

def main():
    app = QApplication([])
    # Create our custom application
    window = SpritePreview()
    # And show it
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
