import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene
from PyQt5.QtGui import QPen, QBrush, QColor
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.pushButton.clicked.connect(self.draw_circles)

    def draw_circles(self):
        self.scene.clear()
        width = self.graphicsView.viewport().width()
        height = self.graphicsView.viewport().height()
        for _ in range(20):
            diameter = random.randint(20, 120)
            x = random.randint(0, max(0, width - diameter))
            y = random.randint(0, max(0, height - diameter))
            pen = QPen(Qt.black)
            pen.setWidth(2)
            brush = QBrush(QColor(255, 255, 0))
            self.scene.addEllipse(x, y, diameter, diameter, pen, brush)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())