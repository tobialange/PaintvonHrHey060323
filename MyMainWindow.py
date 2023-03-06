from PySide6.QtWidgets import QMainWindow, QMenuBar, QLabel, QColorDialog, QFileDialog
from PySide6.QtGui import QColor, QPixmap, QMouseEvent, QPaintEvent, QPainter

class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.menu_bar = QMenuBar(None)

        self.fileMenu = self.menu_bar.addMenu("Bilder")

        self.action_load_file = self.fileMenu.addAction("Bild öffnen", self.load_file)
        self.action_save_file = self.fileMenu.addAction("Bild speichern", self.save_file)

        self.fileMenu.addAction("Farbe", self.setColor)

        self.setMenuBar(self.menu_bar)

        self.setWindowTitle("M$ P41nt")

        self.pos = None
        self.color = QColor("green")
        self.canvas = QPixmap("./Hund.jpg")

        self.draw_Widget = QLabel(self)
        self.draw_Widget.setPixmap(self.canvas)
        self.setCentralWidget(self.draw_Widget)

    def setColor(self):
        selected_color = QColorDialog.getColor(self.color, self, "Farbe wählen")

        if selected_color.isValid():
            self.color = selected_color

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.pos = event.pos()

        self.update()

    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QPainter(self.canvas)

        if self.pos:
            painter.setPen(self.color)
            painter.drawEllipse(self.pos, 10, 10)

        painter.end()
        self.draw_Widget.setPixmap(self.canvas)

    def load_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Bild auswählen", "Bilder (*.png, *.jpg)")

        if file_name:
            self.canvas = QPixmap(file_name)
            self.setPixmap(self.canvas)

            self.update()

    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Bild speichern", "Bilder (*.png, *.jpg)")

        self.canvas.save(file_name)

