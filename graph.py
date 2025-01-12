#The canvas
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import QtWebEngineWidgets

from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QDesktopServices,QPalette, QColor,QPixmap, QAction, QFont

from re import S
import sys
import calc_handler
from PyQt6.QtCore import Qt



from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QStackedLayout, QPushButton, QLabel, QLineEdit, QGraphicsPixmapItem,QStatusBar
from PyQt6.QtGui import QPalette, QColor,QPixmap

import sentiment
import reddit_scraping
from risk_counter import risk_analyzer
from t_scraper2 import Scraper

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import yfinance as yf
import pandas as pd


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=50, height=45, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)
        
#The class for the finance graph
class Graph(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Graph")

        self.sc = MplCanvas(self, width=50, height=45, dpi=100)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

        toolbar = NavigationToolbar(self.sc, self)
        layout = QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(self.sc)

        # Add title of the stock
        self.stock_info_label = QLabel()
        self.stock_info_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.AlignmentFlag.AlignRight)
        font = QFont("Arial", 16, QFont.Weight.Bold)  # Set font size and weight
        self.stock_info_label.setFont(font)
        layout.addWidget(self.stock_info_label)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show()

        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()
        file_menu = menu.addMenu("Settings")
        file_menu.addAction("Options")

        self.needs_update = False

    def update_plot(self):
        try:
            if self.needs_update:
                if hasattr(self, 'stock_data') and not self.stock_data.empty:
                    if 'Close' in self.stock_data.columns:
                        # Validate 'Close' column
                        close_data = self.stock_data['Close']
                        if isinstance(close_data, pd.DataFrame):
                            close_data = close_data.squeeze()  # Convert DataFrame to Series if needed

                        if close_data.empty:
                            print("Error: 'Close' column is empty. Nothing to plot.")
                            return

                        x = self.stock_data.index
                        y = close_data.values  # Ensure it's a 1D numpy array

                        # Clear and plot
                        self.sc.axes.cla()
                        self.sc.axes.plot(x, y, color='green', linewidth=2)
                        self.sc.axes.fill_between(x, y, color='green', alpha=0.3)
                        self.sc.draw()

                        # Update stock info label
                        current_price = close_data.iloc[-1]
                        self.stock_info_label.setText(f"{self.selected_stock}: {current_price:.2f}")
                    else:
                        print("Error: 'Close' column not found in stock_data.")
                else:
                    print("Error: stock_data is empty or invalid.")
            self.needs_update = False
        except Exception as e:
            print(f"Error in update_plot: {e}")


    def onMyToolBarButtonClick(self, symbol):
        print(f"Fetching data for symbol: {symbol}")  # Debugging log
        self.selected_stock = symbol
        self.needs_update = False  # Disable updates until the data is ready

        try:
            # Fetch data from Yahoo Finance
            self.stock_data = yf.download(tickers=symbol, period="1mo", interval="30m")
            if self.stock_data.empty:
                print(f"No data returned for {symbol}. Check the symbol or connection.")  # Debugging log
            else:
                self.needs_update = True
                print("WORKS")
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")  # Debugging log




#The button for the graph( It will display on another window)
'''self.btn = QPushButton("Graph")
self.btn.setCheckable(True)
self.btn.setChecked(True)
self.btn.pressed.connect(self.activate_graph)
button_layout.addWidget(self.btn)

 #Edw paides tha prepei na syndesoume wste na exei ta koumpia apo to app sto graph
def activate_graph(self):
    
    print("Activating Tab 0...")
    try:
        self.graph_window = Graph()
        toolbar = self.graph_window.addToolBar("Stocks")
            
        self.doc = "assets\watch_list.txt"
        stocks = []
        file = open(self.doc,"r")
        for line in file:
            print(line, end='')
            stocks.append(line)


        print(stocks)   
        for stock in stocks:
            button_action = QAction(stock, self.graph_window)
            button_action.setStatusTip("This is your button")
            button_action.triggered.connect(lambda checked, s=stock: self.graph_window.onMyToolBarButtonClick(s))
            toolbar.addAction(button_action)
    except Exception as e:
        print("Error in activate_tab_0:", e)
'''
