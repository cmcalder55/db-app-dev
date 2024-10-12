# Requires PyQt5 or PySide2
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
)
import sys
import json
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from parse_lab_jsons import clean_data
import random
import networkx as nx

def import_data():
    cleaned = clean_data()
    print(json.dumps(cleaned, indent = 4))


class GraphCanvas(FigureCanvas):
    def __init__(self, parent=None):
        fig = Figure()
        self.axes = fig.add_subplot(111)
        super().__init__(fig)

    def plot(self, lab_type=""):
        # Clear previous plot
        self.axes.clear()
        
        # Example: Create a simple graph for demonstration
        G = nx.Graph()
        nodes = range(1, 6)  # Create 5 nodes
        edges = [(1, 2), (1, 3), (3, 4), (4, 5), (2, 5)]  # Define edges
        
        G.add_nodes_from(nodes)
        G.add_edges_from(edges)
        
        # The layout for our nodes
        layout = nx.spring_layout(G)
        
        # Draw the graph according to lab_type if needed
        nx.draw(G, layout, ax=self.axes, with_labels=True, node_size=700, node_color='skyblue')
        
        self.axes.set_title(f'{lab_type} Labyrinth')
        self.draw()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("The Lord's Labyrinth")
        # Set window size
        self.resize(666, 200)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        # Initialize the button actions with a checkable property
        self.button_actions = []
        labs = ["Normal", "Cruel", "Merciless", "Uber"]
        for lab in labs:
            button_action = QAction(lab, self)
            button_action.setStatusTip(f"{lab} Lab")
            button_action.triggered.connect(lambda checked, a=button_action: self.onMyToolBarButtonClick(a))
            button_action.setCheckable(True)
            toolbar.addAction(button_action)
            self.button_actions.append(button_action)
            # Add separator between buttons, except after the last one
            if lab != labs[-1]:  
                toolbar.addSeparator()

        self.setStatusBar(QStatusBar(self))

        self.graph_canvas = GraphCanvas(self)  # Initialize the graph canvas
        self.setCentralWidget(self.graph_canvas)  # Set the graph canvas as the central widget

    def positionWindowTopRight(self):
        # Get the screen size from the application instance
        screen = QApplication.primaryScreen().geometry()
        screenWidth = screen.width()
        screenHeight = screen.height()

        # Calculate position for top right corner
        windowWidth = self.width()
        windowHeight = self.height()
        self.move(screenWidth - windowWidth, 0)  # Move window to top right corner

    def onMyToolBarButtonClick(self, clicked_action):
        # Uncheck all other actions
        for action in self.button_actions:
            if action != clicked_action:
                action.setChecked(False)
        print(f"Displaying {clicked_action.text()} Laboratory Map")

        # Trigger graph update
        self.graph_canvas.plot(clicked_action.text())

if __name__ == "__main__":
    # Create the application instance
    app = QApplication(sys.argv)

    # Create the main window instance
    mainWindow = MainWindow()

    # Position the window at the top right corner
    mainWindow.positionWindowTopRight()

    # Show the main window
    mainWindow.show()

    # Start the application's event loop
    sys.exit(app.exec_())
