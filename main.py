from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import QtWebEngineWidgets
from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtGui import QDesktopServices,QPalette, QColor,QPixmap, QAction, QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QStackedLayout, QPushButton, QLabel, QLineEdit, QGraphicsPixmapItem,QStatusBar

import sys
import calc_handler

import sentiment
import reddit_scraping
from risk_counter import risk_analyzer
from t_scraper2 import Scraper

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import yfinance as yf
import ticker_extractor
from graph import MplCanvas,Graph

user="YOUR_USERNAME"
mail="YOUR_EMAIL"
pas="YOUR_PASSWORD"
x_scrape=Scraper(user,mail,pas)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.slidebar_icons = QtWidgets.QWidget(parent=self.centralwidget)
        self.slidebar_icons.setStyleSheet("background-color: rgb(81, 229, 137);\n"
        "border-radius: 10px;")
        self.slidebar_icons.setHidden(True) #Για να κλείνει στην αρχή το ένα μενού
        self.slidebar_icons.setObjectName("slidebar_icons")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.slidebar_icons)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scele_bt_icon = QtWidgets.QPushButton(parent=self.slidebar_icons)
        self.scele_bt_icon.setStyleSheet("height: 30px;\n"
        "border: none;")
        self.scele_bt_icon.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/3 lines.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.scele_bt_icon.setIcon(icon)
        self.scele_bt_icon.setCheckable(True)
        self.scele_bt_icon.setObjectName("scele_bt_icon")
        self.verticalLayout_5.addWidget(self.scele_bt_icon)
        self.verticalLayout_top3_icon = QtWidgets.QVBoxLayout()
        self.verticalLayout_top3_icon.setObjectName("verticalLayout_top3_icon")
        self.home_bt_icon = QtWidgets.QPushButton(parent=self.slidebar_icons)
        self.home_bt_icon.setStyleSheet("height: 30px;\n"
        "border: none;")
        self.home_bt_icon.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/home icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon1.addPixmap(QtGui.QPixmap("Icons/home icon fill.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.home_bt_icon.setIcon(icon1)
        self.home_bt_icon.setCheckable(True)
        self.home_bt_icon.setAutoExclusive(True)
        self.home_bt_icon.setObjectName("home_bt_icon")
        self.verticalLayout_top3_icon.addWidget(self.home_bt_icon)
        self.watchlist_bt_icon = QtWidgets.QPushButton(parent=self.slidebar_icons)
        self.watchlist_bt_icon.setStyleSheet("height: 30px;\n"
        "border: none;")
        self.watchlist_bt_icon.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/star icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon2.addPixmap(QtGui.QPixmap("Icons/star icon fill.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.watchlist_bt_icon.setIcon(icon2)
        self.watchlist_bt_icon.setCheckable(True)
        self.watchlist_bt_icon.setAutoExclusive(True)
        self.watchlist_bt_icon.setObjectName("watchlist_bt_icon")
        self.verticalLayout_top3_icon.addWidget(self.watchlist_bt_icon)
        self.coins_bt_icon = QtWidgets.QPushButton(parent=self.slidebar_icons)
        self.coins_bt_icon.setStyleSheet("height: 30px;\n"
        "border: none;")
        self.coins_bt_icon.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icons/coin icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon3.addPixmap(QtGui.QPixmap("Icons/coin icon fill.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.coins_bt_icon.setIcon(icon3)
        self.coins_bt_icon.setCheckable(True)
        self.coins_bt_icon.setAutoExclusive(True)
        self.coins_bt_icon.setObjectName("coins_bt_icon")
        self.verticalLayout_top3_icon.addWidget(self.coins_bt_icon)
        self.verticalLayout_5.addLayout(self.verticalLayout_top3_icon)
        spacerItem = QtWidgets.QSpacerItem(28, 117, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.verticalLayout_top2_icon = QtWidgets.QVBoxLayout()
        self.verticalLayout_top2_icon.setObjectName("verticalLayout_top2_icon")
        self.fredom24_bt_icon = QtWidgets.QPushButton(parent=self.slidebar_icons)
        self.fredom24_bt_icon.setStyleSheet("height: 30px;\n"
        "border: none;")
        self.fredom24_bt_icon.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Icons/freedom logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.fredom24_bt_icon.setIcon(icon4)
        self.fredom24_bt_icon.setCheckable(True)
        self.fredom24_bt_icon.setAutoExclusive(True)
        self.fredom24_bt_icon.setObjectName("fredom24_bt_icon")
        self.verticalLayout_top2_icon.addWidget(self.fredom24_bt_icon)
        self.Trading212_bt_icon = QtWidgets.QPushButton(parent=self.slidebar_icons)
        self.Trading212_bt_icon.setStyleSheet("height: 30px;\n"
        "border: none;")
        self.Trading212_bt_icon.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Icons/Trading212.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Trading212_bt_icon.setIcon(icon5)
        self.Trading212_bt_icon.setCheckable(True)
        self.Trading212_bt_icon.setAutoExclusive(True)
        self.Trading212_bt_icon.setObjectName("Trading212_bt_icon")
        self.verticalLayout_top2_icon.addWidget(self.Trading212_bt_icon)
        self.verticalLayout_5.addLayout(self.verticalLayout_top2_icon)
        spacerItem1 = QtWidgets.QSpacerItem(28, 158, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.settings_bt_icon = QtWidgets.QPushButton(parent=self.slidebar_icons)
        self.settings_bt_icon.setStyleSheet("height: 30px;\n"
        "border: none;")
        self.settings_bt_icon.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Icons/Settings icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon6.addPixmap(QtGui.QPixmap("Icons/Settings icon fill.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.settings_bt_icon.setIcon(icon6)
        self.settings_bt_icon.setCheckable(True)
        self.settings_bt_icon.setAutoExclusive(True)
        self.settings_bt_icon.setObjectName("settings_bt_icon")
        self.verticalLayout_5.addWidget(self.settings_bt_icon)
        self.gridLayout.addWidget(self.slidebar_icons, 0, 0, 1, 1)
        self.main_window = QtWidgets.QWidget(parent=self.centralwidget)
        self.main_window.setObjectName("main_window")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_window)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(parent=self.main_window)
        self.widget.setStyleSheet("background-color: rgb(81, 229, 137);\n"
        "border-radius: 15px;")
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Icons/logo-big.png"))
        self.label.setObjectName("label")
        self.label.mousePressEvent = self.easter_egg #emj
        self.horizontalLayout_3.addWidget(self.label)
        #
        
        self.widget_2 = QtWidgets.QWidget(parent=self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.searchbar = QtWidgets.QLineEdit(parent=self.widget_2)
        #self.searchbar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.searchbar.setClearButtonEnabled(True)
        self.searchbar.setObjectName("searchbar")
        #self.horizontalLayout_2.addWidget(self.searchbar)
        self.searchbox_bt = QtWidgets.QPushButton(parent=self.widget_2)
        #self.searchbox_bt.setStyleSheet("background-color: rgb(255, 255, 255);")
        #self.searchbox_bt.setText("")
        #icon7 = QtGui.QIcon()
        #icon7.addPixmap(QtGui.QPixmap("Icons/search icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        #self.searchbox_bt.setIcon(icon7)
        #self.searchbox_bt.setObjectName("searchbox_bt")
        #self.horizontalLayout_2.addWidget(self.searchbox_bt)
        self.horizontalLayout_3.addWidget(self.widget_2)
        self.verticalLayout.addWidget(self.widget)
        #
        self.stackedWidget_pages = QtWidgets.QStackedWidget(parent=self.main_window)
        self.stackedWidget_pages.setStyleSheet("")
        self.stackedWidget_pages.setObjectName("stackedWidget_pages")
        #----------------------------------------watchlist tab
        self.watchlist_stack = QtWidgets.QWidget()
        self.watchlist_stack.setObjectName("watchlist_stack")
        self.watchlist_title_label = QtWidgets.QLabel(parent=self.watchlist_stack)
        self.watchlist_title_label.setGeometry(QtCore.QRect(30, 20, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.watchlist_title_label.setFont(font)
        self.watchlist_title_label.setObjectName("watchlist_title_label")
        #self.stackedWidget_pages.addWidget(self.watchlist_stack)
        #-----------------------------
        subLay1 = QVBoxLayout()
        watch_list_layout = QGridLayout()
        
        #making 5 labels to keep track of predetermined investments?
        #2 of those five labels will be hidden until they are added beacasue i do not know how to make it possible to add more 
        # that is a major skill issue on my part but you do not need more than five labels trust
        # also the user does not need to know that l+ratio
        self.list_label1 = QLabel("")
        self.list_label1.setMaximumWidth(450)
        self.list_label1.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)
        self.list_label1.setStyleSheet("""background-color: lightGray;
                                        font-family: Titillium;
                                        font-size: 18px;
                                        border: 4px inset darkGray;
                                        """)
        #self.list_label1.setStyleSheet('border: 1px solid #0d6efd; ')
        subLay1.addWidget(self.list_label1)

        self.list_label2 = QLabel("")
        self.list_label2.setMaximumWidth(450)
        self.list_label2.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)
        self.list_label2.setStyleSheet("""background-color: lightGray;
                                        font-family: Titillium;
                                        font-size: 18px;
                                        border: 4px inset darkGray;
                                        """)
        subLay1.addWidget(self.list_label2)


        self.list_label3 = QLabel("")
        self.list_label3.setMaximumWidth(450)
        self.list_label3.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)
        self.list_label3.setStyleSheet("""background-color: lightGray;
                                        font-family: Titillium;
                                        font-size: 18px; 
                                        border: 4px inset darkGray;
                                        """)
        subLay1.addWidget(self.list_label3)

        self.list_label4 = QLabel('')
        self.list_label4.setMaximumWidth(450)
        self.list_label4.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)
        self.list_label4.setStyleSheet("""background-color: lightGray;
                                        font-family: Titillium;
                                        font-size: 18px;
                                        border: 4px inset darkGray;
                                        """)
        
        subLay1.addWidget(self.list_label4)

        self.list_label5 = QLabel('')
        self.list_label5.setMaximumWidth(450)
        self.list_label5.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)
        self.list_label5.setStyleSheet("""background-color: lightGray;
                                        font-family: Titillium;
                                        font-size: 18px;
                                        border: 4px inset darkGray;
                                        """)
        
        


        subLay1.addWidget(self.list_label5)

        self.list_label1.mousePressEvent = self.watch_list_1
        self.list_label2.mousePressEvent = self.watch_list_2
        self.list_label3.mousePressEvent = self.watch_list_3
        self.list_label4.mousePressEvent = self.watch_list_4
        self.list_label5.mousePressEvent = self.watch_list_5

        
        #------------------add and remove labels customizability
        self.watch_list_length = 0 #num of labels 3 pre cut and 2 custom

        #store watchlist in file
        self.doc = "assets\watch_list.txt" #path for watchlist
        file = open(self.doc,"r")
        i = 0 #basically a count
        self.list_labels=[]
        #creates 5 empty labels
        self.list_labels.append(self.list_label1)
        self.list_labels.append(self.list_label2)
        self.list_labels.append(self.list_label3)
        self.list_labels.append(self.list_label4)
        self.list_labels.append(self.list_label5)
        
        self.listw=['','','','','']#create a list which coresponds to labels
        for line in file:#loops the file
                if line[len(line)-1:]=='\n':#if the last character is \n it removes it
                        line=line[:len(line)-1]
                self.listw[i]=line#every item from file goes to the listw
                self.list_labels[i].setText(self.listw[i])#connects listw with labels
                i+=1
        for i in range(5):
                #hides the labels without writing anything
                if self.list_labels[i].text()!='':
                        self.list_labels[i].show()
                        self.watch_list_length+=1
                else:
                        self.list_labels[i].hide()
        file.close()








                                
                                
                                

        sub_of_sublay1 = QHBoxLayout()

        self.add_button = QPushButton("Add to list")
        self.add_button.setFixedHeight(30)
        self.remove_button = QPushButton("Remove from list")
        self.remove_button.setFixedHeight(30)
        self.save_button = QPushButton("Save list")
        self.save_button.setFixedHeight(30)
        
        self.add_button.clicked.connect(self.add_to_list)
        self.remove_button.clicked.connect(self.remove_from_list)
        self.save_button.clicked.connect(self.save_list)
        
        sub_of_sublay1.addWidget(self.add_button)
        sub_of_sublay1.addWidget(self.remove_button)
        sub_of_sublay1.addWidget(self.save_button)


        sub_sublay = QWidget()
        sub_sublay.setLayout(sub_of_sublay1)

        subLay1.addWidget(sub_sublay)

        #self.graph_but = QPushButton("Graph")
        #self.graph_but.setCheckable(True)
        #self.graph_but.setChecked(True)

        #self.graph_but.clicked.connect(self.activate_graph)
        #subLay1.addWidget(self.graph_but)
        

        self.line1 = QLineEdit()
        self.line1.setMinimumHeight(25)
        self.line1.setStyleSheet(""" 
                                background-color: lightGray;
                                font-family: Titillium;
                                font-size: 14px;
                                        """)
        subLay1.addWidget(self.line1)
        self.line1.setAlignment(Qt.AlignmentFlag.AlignBottom)

        self.line1.mousePressEvent = self.clicked_line
        sub_but_lay = QHBoxLayout()

        self.buton = QPushButton("Search")
        self.buton.setCheckable(True)
        self.buton.clicked.connect(self.the_btn_click)
        self.buton.setMinimumWidth(150)
        self.buton.setMinimumHeight(50)
        self.buton.setStyleSheet(""" background-color: rgb(145, 200, 170);
                                font-family: Titillium;
                                font-size: 14px;
                                border: 1px inset black;
                                """)

                              
        
        sub_but_lay.addWidget(self.buton)

        self.graph_but = QPushButton("Graph")
        self.graph_but.setCheckable(True)
        self.graph_but.setMinimumWidth(150)
        self.graph_but.setMinimumHeight(50)
        self.graph_but.setStyleSheet(""" 
                                        background-color: green;
                                        font-family: Titillium;
                                        font-size: 14px;
                                        border: 1px inset black;
                                        
                                        """)

        #self.graph_but.setChecked(True)
        self.graph_but.clicked.connect(self.activate_graph)

        sub_but_lay.addWidget(self.graph_but)

        butt_wid = QWidget()

        butt_wid.setLayout(sub_but_lay)

        subLay1.addWidget(butt_wid)

        #col_layout.addWidget(Color("blue"),0,0)
        #col_layout.addWidget(Color("green"),0,1)
        get = QWidget()
        get.setLayout(subLay1)
        get.setMaximumWidth(450)
        #get.autoFillBackground()

        #get.palette = self.palette()
        #get.palette.setColor(QPalette.ColorRole.Window, QColor("red"))
        #get.setPalette(get.palette)

        watch_list_layout.addWidget(get,0,0)
        #--------------------------------------------------- left side of grid tab

        right_lay = QVBoxLayout()

        

        self.top_l = QLabel("Twitter-X box")
        #self.top_l.setFixedWidth(400)
        self.left_l = QLabel("Reddit box")
        self.right_l = QLabel("Sentiment Analysis")
        self.right_l.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.top_l.setStyleSheet("""
                                background-color: rgb(145, 200, 170);
                                font-family: Raleway;
                                font-size: 18px;
                                border: 3px inset black;
                                """)
        self.left_l.setStyleSheet("""
                                background-color: rgb(145, 200, 170);
                                font-family: Raleway;
                                font-size: 18px;
                                border: 3px inset black;
                                """)
        self.right_l.setStyleSheet(""" 
                                        background-color:  rgb(81, 229, 137);
                                        font-family: Raleway;
                                        font-size: 20px;
                                        border: 3px inset black;
                                        """)

        right_lay.addWidget(self.right_l)
        right_lay.addWidget(self.top_l)
        right_lay.addWidget(self.left_l)
        

        col = QWidget()
        col.setStyleSheet('background-color: lightGray')
        col.setMaximumWidth(550)
        col.setLayout(right_lay)
        watch_list_layout.addWidget(col,0,1) #----right side of widget

        list_wid = QWidget()
        list_wid.setLayout(watch_list_layout)

        self.stackedWidget_pages.addWidget(list_wid)

        #-----------------------------------------watchlist tab end
        
        self.coins_stack = QtWidgets.QWidget()
        self.coins_stack.setObjectName("coins_stack")
        
        self.coins_conventer_engine = QtWebEngineWidgets.QWebEngineView()
        #self.coins_conventer_engine.setGeometry(QtCore.QRect(10, 40, 531, 411))
        self.coins_conventer_engine.setUrl(QtCore.QUrl("https://wise.com/gr/currency-converter/fx-widget/converter?sourceCurrency=GBP&targetCurrency=EUR"))
        self.coins_conventer_engine.setObjectName("coins_conventer_engine")

        self.watchlist_title_label_2 = QtWidgets.QLabel()
        self.watchlist_title_label_2.setGeometry(QtCore.QRect(10, 10, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.watchlist_title_label_2.setFont(font)
        self.watchlist_title_label_2.setObjectName("watchlist_title_label_2")
        coin_lay = QVBoxLayout()
        coin_lay.addWidget(self.watchlist_title_label_2)
        coin_lay.addWidget(self.coins_conventer_engine)
        coin_lay.setAlignment(Qt.AlignmentFlag.AlignCenter)
        

        self.coins_stack.setLayout(coin_lay)
        self.stackedWidget_pages.addWidget(self.coins_stack)
        

        
        #--------email thingamajig start
        self.settings_stack = QtWidgets.QWidget()
        self.settings_stack.setObjectName("settings_stack")
        #here imma do email noification
        email_tab_layout =  QVBoxLayout()
        #email_first_lay = QVBoxLayout()
        email_sec_lay = QHBoxLayout()
        email_third_lay = QVBoxLayout()

        email_first_Label = QLabel("Do you want to \n stay updated via e-mail?")
        email_tab_layout.addWidget(email_first_Label)
        email_first_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        email_first_Label.setStyleSheet("""
                                        background-color: rgb(81, 229, 137);
                                        font-family: Raleway;
                                        font-size: 20px;
                                        border: 3px inset black;
                                        """)
            #second widget
        self.email_btn_y = QPushButton("Yes")
        self.email_btn_n = QPushButton("No")

        self.email_btn_y.setStyleSheet("""
                                        background-color: green;
                                        font-family: Titillium;
                                        font-size: 20px;
                                        border: 3px inset black;
                                        """)
        self.email_btn_n.setStyleSheet("""
                                        background-color: red;
                                        font-family: Titillium;
                                        font-size: 20px;
                                        border: 3px inset black;
                                        """)

        self.email_btn_y.setCheckable(True)
        self.email_btn_n.setCheckable(True)
        self.email_btn_n.setChecked(True)
        self.email_btn_y.clicked.connect(self.email_yes_click)
        self.email_btn_n.clicked.connect(self.email_no_click)

        self.email_btn_n.setMaximumWidth(200)
        self.email_btn_n.setMaximumHeight(80)
        

        self.email_btn_y.setMaximumWidth(200)
        self.email_btn_y.setMaximumHeight(80)
        

        email_sec_lay.addWidget(self.email_btn_y)
        email_sec_lay.addWidget(self.email_btn_n)

        email_sec_widget = QWidget()
        email_sec_widget.setLayout(email_sec_lay)
        email_sec_widget.setStyleSheet('background-color: rgb(145, 200, 170)')

        email_tab_layout.addWidget(email_sec_widget)
            #third widget of the page

        email_3label = QLabel("If yes enter your e-mail:")
        email_3label.setStyleSheet(""" 
                                        background-color:  rgb(145, 200, 170);
                                        font-family: Raleway;
                                        font-size: 20px;
                                        border: 3px inset black;
                                        """)
        self.email_line = QLineEdit()
        self.email_line.setStyleSheet(""" 
                                background-color: lightGray;
                                font-family: Titillium;
                                font-size: 14px;
                                        """)
        self.email_line.setMinimumHeight(35)

        email_third_lay.addWidget(email_3label)
        email_third_lay.addWidget(self.email_line)

        email_third_widget = QWidget()
        email_third_widget.setLayout(email_third_lay)
        email_third_widget.setStyleSheet('background-color: rgb(145, 200, 170)')

        #self.email_line.setStyleSheet('background-color: white')

        email_tab_layout.addWidget(email_third_widget)
        email_tab_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        email_tab_layout.setContentsMargins(100 , 25 , 100 , 25)

        #button distance from each other
        #self.email_btn_y.setContentsMargins(25 , 25 , 25 , 25)
        #self.email_btn_n.setContentsMargins(25 , 25 , 25 , 25)

        self.settings_stack.setLayout(email_tab_layout)
        #self.settings_stack.setStyleSheet('border:4px inset lightGray')
        

        self.stackedWidget_pages.addWidget(self.settings_stack)
        




        #email_widget = QWidget()
        #email_widget.setLayout(email_tab_layout)

        #email thingamajig end----------
        #why is this at the bottom---------------------------------------------home page layout

        self.Home_stack = QtWidgets.QWidget()
        self.Home_stack.setObjectName("Home_stack")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Home_stack)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.home_title_label = QtWidgets.QLabel()
        #sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        #sizePolicy.setHorizontalStretch(0)
        #sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.home_title_label.sizePolicy().hasHeightForWidth())
        #self.home_title_label.setSizePolicy(sizePolicy)
        #font = QtGui.QFont()
        #font.setPointSize(14)
        #self.home_title_label.setFont(font)
        #self.home_title_label.setObjectName("home_title_label")
        home_lab = QLabel("Καλώς Ήρθατε στην Pythia!") #homepage title label
        home_lab.setStyleSheet("""background-color: rgb(145, 200, 170);
                                font-family: Titillium;
                                font-size: 22px;
                                border: 3px inset black""")
        font= QtGui.QFont()
        font.setBold(True)
        home_lab.setFont(font)
        home_lab.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_2.addWidget(home_lab)
        #homepage text label
        home_sub = QLabel("""Οδηγίες:
                          \nΣτην καρτέλα "Ακολουθώ" βρίσκεται η κυρια λίστα της εφαρμογής.
                          \nΓια προσθήκη ενός στοιχείου στην λίστα, γράψτε στο πεδίο κειμένου και πατήστε το κουμπί "Add to list"
                          \nΓια αφαίρεση ενός στοιχείου από τη λίστα, 
                          \n    γράψτε το όνομα του στοιχείου  στο πεδίο κειμένου και πατήστε το κουμπί "Remove from list" 
                          \nΓια αφαίρεση του τελευταίου στοιχείου της λίστας πατήστε το κουμπί "Remove from list" (άδειο πεδίο κειμένου)
                          \nΓια αποθήκευση της λίστας πατήστε το κουμπί "save list"
                          \nΓια εκτίμηση ενός στοιχείου διαλέξτε το στοιχείο από την παραπάνω λίστα ή γράψτε ότι σας ενδιαφέρι και πατήστε το κουμπί "search" 
                          \nΓια εμφάνιση γραφημάτων πατήστε το κουμπί "Graph"
                          \n             
                          \n Για να λαβαίνετε ειδοποιήσεις μεταβείτε στις "ρυθμίσεις" δώστε το e-mail σας στο πλαίσιο κειμένου και πατήστε "Ναι"
                          \n Αν θέλετε να σταματήσετε την αποστολή ειδοποιήσεων απλώς πατήστε "Όχι"
                          \n """)

        home_sub.setStyleSheet("""background-color: rgb(145, 200, 170);
                                font-family: Titillium;
                                font-size: 20px;
                                border: 3px inset black""")
        home_sub.setAlignment(Qt.AlignmentFlag.AlignCenter)


        self.verticalLayout_2.addWidget(home_sub)

        #self.verticalLayout_2.addWidget(self.home_title_label)
        #self.live_statistics = QtWebEngineWidgets.QWebEngineView(parent=self.Home_stack)
        #self.live_statistics.setUrl(QtCore.QUrl("https://www.tradingview.com/heatmap/stock/#%7B%22dataSource%22%3A%22AllUSA%22%2C%22blockColor%22%3A%22change%22%2C%22blockSize%22%3A%22market_cap_basic%22%2C%22grouping%22%3A%22sector%22%7D"))
        #self.live_statistics.setZoomFactor(0.5)
        #self.live_statistics.setObjectName("live_statistics")
        #self.verticalLayout_2.addWidget(self.live_statistics)
        self.stackedWidget_pages.addWidget(self.Home_stack)
        self.verticalLayout.addWidget(self.stackedWidget_pages)
        self.gridLayout.addWidget(self.main_window, 0, 2, 1, 1)
        self.menu_text = QtWidgets.QWidget(parent=self.centralwidget)
        self.menu_text.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_text.sizePolicy().hasHeightForWidth())
        self.menu_text.setSizePolicy(sizePolicy)
        self.menu_text.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.menu_text.setStyleSheet("background-color: rgb(81, 229, 137);\n"
"border-radius: 10px;")
        self.menu_text.setObjectName("menu_text")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.menu_text)
        self.gridLayout_2.setContentsMargins(-1, -1, 9, -1)
        self.gridLayout_2.setSpacing(9)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scale_bt_icon = QtWidgets.QPushButton(parent=self.menu_text)
        self.scale_bt_icon.setStyleSheet("height: 30px;\n"
"border: none;")
        self.scale_bt_icon.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("Icons/x movement.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.scale_bt_icon.setIcon(icon8)
        self.scale_bt_icon.setCheckable(True)
        self.scale_bt_icon.setObjectName("scale_bt_icon")
        self.horizontalLayout.addWidget(self.scale_bt_icon)
        spacerItem2 = QtWidgets.QSpacerItem(48, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout_top3_text = QtWidgets.QVBoxLayout()
        self.verticalLayout_top3_text.setObjectName("verticalLayout_top3_text")
        self.home_bt_text = QtWidgets.QPushButton(parent=self.menu_text)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home_bt_text.sizePolicy().hasHeightForWidth())
        self.home_bt_text.setSizePolicy(sizePolicy)
        self.home_bt_text.setStyleSheet("text-align: left;\n"
"height: 30px;\n"
"border: none;\n"
"\n"
"QPushButton#pushButton:checked {\n"
" color: black; background-color: green;\n"
"}")
        self.home_bt_text.setIcon(icon1)
        self.home_bt_text.setCheckable(True)
        self.home_bt_text.setAutoExclusive(True)
        self.home_bt_text.setObjectName("home_bt_text")
        self.verticalLayout_top3_text.addWidget(self.home_bt_text)
        self.watchlist_bt_text = QtWidgets.QPushButton(parent=self.menu_text)
        self.watchlist_bt_text.setStyleSheet("text-align: left;\n"
"height: 30px;\n"
"border: none;")
        self.watchlist_bt_text.setIcon(icon2)
        self.watchlist_bt_text.setCheckable(True)
        self.watchlist_bt_text.setAutoExclusive(True)
        self.watchlist_bt_text.setObjectName("watchlist_bt_text")
        self.verticalLayout_top3_text.addWidget(self.watchlist_bt_text)
        self.coins_bt_text = QtWidgets.QPushButton(parent=self.menu_text)
        self.coins_bt_text.setStyleSheet("text-align: left;\n"
"height: 30px;\n"
"border: none;")
        self.coins_bt_text.setIcon(icon3)
        self.coins_bt_text.setCheckable(True)
        self.coins_bt_text.setAutoExclusive(True)
        self.coins_bt_text.setObjectName("coins_bt_text")
        self.verticalLayout_top3_text.addWidget(self.coins_bt_text)
        self.gridLayout_2.addLayout(self.verticalLayout_top3_text, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(28, 126, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 2, 0, 1, 1)
        self.verticalLayout_top2_text = QtWidgets.QVBoxLayout()
        self.verticalLayout_top2_text.setObjectName("verticalLayout_top2_text")
        self.fredomm24_bt_text = QtWidgets.QPushButton(parent=self.menu_text)
        self.fredomm24_bt_text.setStyleSheet("text-align: left;\n"
"height: 30px;\n"
"border: none;")
        self.fredomm24_bt_text.setIcon(icon4)
        self.fredomm24_bt_text.setCheckable(True)
        self.fredomm24_bt_text.setAutoExclusive(True)
        self.fredomm24_bt_text.setObjectName("fredomm24_bt_text")
        self.verticalLayout_top2_text.addWidget(self.fredomm24_bt_text)
        self.trading212_bt_text = QtWidgets.QPushButton(parent=self.menu_text)
        self.trading212_bt_text.setStyleSheet("text-align: left;\n"
"height: 30px;\n"
"border: none;\n"
"")
        self.trading212_bt_text.setIcon(icon5)
        self.trading212_bt_text.setCheckable(True)
        self.trading212_bt_text.setAutoExclusive(True)
        self.trading212_bt_text.setObjectName("trading212_bt_text")
        self.verticalLayout_top2_text.addWidget(self.trading212_bt_text)
        self.gridLayout_2.addLayout(self.verticalLayout_top2_text, 3, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(28, 153, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 4, 0, 1, 1)
        self.settings_bt_text = QtWidgets.QPushButton(parent=self.menu_text)
        self.settings_bt_text.setStyleSheet("text-align: left;\n"
"height: 30px;\n"
"border: none;")
        self.settings_bt_text.setIcon(icon6)
        self.settings_bt_text.setCheckable(True)
        self.settings_bt_text.setAutoExclusive(True)
        self.settings_bt_text.setObjectName("settings_bt_text")
        self.gridLayout_2.addWidget(self.settings_bt_text, 5, 0, 1, 1)
        self.gridLayout.addWidget(self.menu_text, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget_pages.setCurrentIndex(3)
        self.scele_bt_icon.toggled['bool'].connect(self.menu_text.setVisible) # type: ignore
        self.scele_bt_icon.toggled['bool'].connect(self.slidebar_icons.setHidden) # type: ignore
        self.scale_bt_icon.toggled['bool'].connect(self.menu_text.setHidden) # type: ignore
        self.scale_bt_icon.toggled['bool'].connect(self.slidebar_icons.setVisible) # type: ignore
        self.home_bt_text.toggled['bool'].connect(self.home_bt_icon.setChecked) # type: ignore
        self.watchlist_bt_text.toggled['bool'].connect(self.watchlist_bt_icon.setChecked) # type: ignore
        self.coins_bt_text.toggled['bool'].connect(self.coins_bt_icon.setChecked) # type: ignore
        self.fredomm24_bt_text.toggled['bool'].connect(self.fredom24_bt_icon.setChecked) # type: ignore
        self.trading212_bt_text.toggled['bool'].connect(self.Trading212_bt_icon.setChecked) # type: ignore
        self.Trading212_bt_icon.toggled['bool'].connect(self.trading212_bt_text.setChecked) # type: ignore
        self.fredom24_bt_icon.toggled['bool'].connect(self.fredomm24_bt_text.setChecked) # type: ignore
        self.coins_bt_icon.toggled['bool'].connect(self.coins_bt_text.setChecked) # type: ignore
        self.watchlist_bt_icon.toggled['bool'].connect(self.watchlist_bt_text.setChecked) # type: ignore
        self.home_bt_icon.toggled['bool'].connect(self.home_bt_text.setChecked) # type: ignore
        self.settings_bt_icon.toggled['bool'].connect(self.settings_bt_text.setChecked) # type: ignore
        self.settings_bt_text.toggled['bool'].connect(self.settings_bt_icon.setChecked) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.home_bt_icon.setToolTip(_translate("MainWindow", "<html><head/><body><p>φφφ</p></body></html>"))
        self.watchlist_title_label.setText(_translate("MainWindow", "Λίστα παρακολούθησης"))
        self.watchlist_title_label_2.setText(_translate("MainWindow", "Μετατροπέας Συναλλάγματος"))
        #self.settings_title_label.setText(_translate("MainWindow", "Ρυθμίσεις"))
        ##self.notificatios_checkBox.setText(_translate("MainWindow", "Ενεργές Ειδοποιήσεις"))
        #self.notificatios_checkBox.setStyleSheet("border: 0px ;") # χρειαζετε γιατι άλλαξα ιδιότητα στο group widget
        ##self.import_email_field.setStyleSheet("border: 0px ;") # χρειαζετε γιατι άλλαξα ιδιότητα στο group widget
        #self.email_check_bt.setText(_translate("MainWindow", "✅"))
        #self.email_check_bt.setStyleSheet("border: 0px ;") # χρειαζετε γιατι άλλαξα ιδιότητα στο group widget
        self.home_title_label.setText(_translate("MainWindow", "Αρχική"))
        self.home_bt_text.setText(_translate("MainWindow", "Αρχική"))
        self.watchlist_bt_text.setText(_translate("MainWindow", "Ακολουθώ               ")) #αυτό το κενό είναι για το πλάτος του menu
        self.coins_bt_text.setText(_translate("MainWindow", "Συνάλλαγμα"))
        self.fredomm24_bt_text.setText(_translate("MainWindow", "Fredom24"))
        self.trading212_bt_text.setText(_translate("MainWindow", "Trading212"))
        self.settings_bt_text.setText(_translate("MainWindow", "Ρυθμίσεις"))

        #connecting buttons for page changing
        self.home_bt_text.clicked.connect(lambda: self.stackedWidget_pages.setCurrentIndex(3))
        self.home_bt_icon.clicked.connect(lambda: self.stackedWidget_pages.setCurrentIndex(3))

        self.watchlist_bt_text.clicked.connect(lambda: self.stackedWidget_pages.setCurrentIndex(0))
        self.watchlist_bt_icon.clicked.connect(lambda: self.stackedWidget_pages.setCurrentIndex(0))

        self.coins_bt_icon.clicked.connect(lambda: self.stackedWidget_pages.setCurrentIndex(1))
        self.coins_bt_text.clicked.connect(lambda: self.stackedWidget_pages.setCurrentIndex(1))

        self.settings_bt_text.clicked.connect(lambda: self.stackedWidget_pages.setCurrentIndex(2))
        self.settings_bt_icon.clicked.connect(lambda: self.stackedWidget_pages.setCurrentIndex(2))

        self.fredomm24_bt_text.clicked.connect(self.freedom24_link)
        self.fredom24_bt_icon.clicked.connect(self.freedom24_link)
        
        self.trading212_bt_text.clicked.connect(self.trading212_link)
        self.Trading212_bt_icon.clicked.connect(self.trading212_link)
        
        #Changing between the pages
    def Home_stack(self):
        self.stackedWidget.setCurrentIndex(0)

    def watchlist_stack(self):
        self.stackedWidget.setCurrentIndex(1)

    def coins_stack(self):
        self.stackedWidget.setCurrentIndex(2)

    def settings_stack(self):
        self.stackedWidget.setCurrentIndex(3)

    def freedom24_link(self):
        url = QUrl("https://freedom24.com/authentication/login?__lang__=el")
        QDesktopServices.openUrl(url)

    def trading212_link(self):
        url = QUrl("https://www.trading212.com/el?login=")
        QDesktopServices.openUrl(url)
    def the_btn_click(self):
                key = self.line1.text()#takes everything written in placeholder
                self.buton.setChecked(False)
                self.right_l.setText("Sentiment Analysis:\n"+ self.line1.text())
                
                try:
                        x_scrape.extract_tweets(key,100)#searches tweets in X
                        #sentiment analysis
                        positive,negative,neutral,comp_index=sentiment.sentiment_vader(x_scrape.tweet_texts)

                        print("Vader -->",positive,negative,neutral)
                        #risk analysis
                        risk=risk_analyzer(positive,negative,neutral)
                        risk.risk_taken()
                        print("from X -->",risk.risk)
                        #prints results
                        self.top_l.setText("From X -->"+str(risk.risk)+"\nVader -->"+"\nPositive: "+str(positive)+"\nNegative: "+str(negative)+"\nNeutral: "+str(neutral))
                        #watch_list.add(key)
                        #stroes the results in csv files
                        string_data=key+','+str(positive)+','+str(negative)+','+str(neutral)+','+risk.risk+','+str(comp_index)+'\n'
                        with open('assets/results_x.csv','a') as data_x:
                                data_x.write(string_data)
                except:
                        print("error with X. try on reddit")
                try:
                        #searches in Reddit
                        reddit=reddit_scraping.ex_reddit(key)
                        positive,negative,neutral,comp_index=sentiment.sentiment_vader(reddit)
                        print("Vader -->",positive,negative,neutral)
                        risk=risk_analyzer(positive,negative,neutral)
                        risk.risk_taken()
                        print("from reddit ->",risk.risk)

                        self.left_l.setText("From Reddit -->"+str(risk.risk)+"\nVader -->"+"\nPositive: "+str(positive)+"\nNegative: "+str(negative)+"\nNeutral: "+str(neutral))
                        #watch_list.add(key)
                        string_data=+key+','+str(positive)+','+str(negative)+','+str(neutral)+','+risk.risk+','+str(comp_index)+'\n'
                        with open('assets/results_reddit.csv','a') as data_reddit:
                                data_reddit.write(string_data)
                except:
                        print("error with reddit")

        #-------------------------------------------------------------list clicks
    def watch_list_1(self,event):
                #print("works\n")
                self.list_label1.setStyleSheet("""background-color: darkGray;
                                        font-family: Titillium;
                                        font-size: 18px;
                                        border: 4px inset black;
                                        """)
                self.list_label2.setStyleSheet("""background-color: lightGray;
                                        font-family: Titillium;
                                        font-size: 18px;
                                        border: 4px inset darkGray;
                                        """)
                self.list_label3.setStyleSheet("""background-color: lightGray;
                                        font-family: Titillium;
                                        font-size: 18px;
                                        border: 4px inset darkGray;
                                        """)
                self.list_label5.setStyleSheet("""background-color: lightGray;
                                        font-family: Titillium;
                                        font-size: 18px;
                                        border: 4px inset darkGray;
                                        """)
                self.list_label4.setStyleSheet("""background-color: lightGray;
                                        font-family: Titillium;
                                        font-size: 18px;
                                        border: 4px inset darkGray;
                                        """)
                temp = self.list_label1.text()
                self.line1.setText(str(temp)) #takes the text frtom the list and inserts it into the program startup
    def watch_list_2(self,event):
                #print("works\n")
                self.list_label2.setStyleSheet("""background-color: darkGray;
                                        font-family: Titillium;
                                        font-size: 18px;
                                        border: 4px inset black;
                                        """) 
                self.list_label1.setStyleSheet("""background-color: lightGray;
                                        font-family: Titillium;
                                        font-size: 18px;
                                        border: 4px inset darkGray;
                                        """)
                self.list_label3.setStyleSheet("""background-color: lightGray;
                                        font-family: Titillium;
                                        font-size: 18px;
                                        border: 4px inset darkGray;
                                        """)
                self.list_label5.setStyleSheet("""background-color: lightGray;
                                        font-family: Titillium;
                                        font-size: 18px;
                                        border: 4px inset darkGray;
                                        """)
                self.list_label4.setStyleSheet("""background-color: lightGray;
                                        font-family: Titillium;
                                        font-size: 18px;
                                        border: 4px inset darkGray;
                                        """) 
                temp = self.list_label2.text()
                self.line1.setText(str(temp))
    def watch_list_3(self,event):
                #print("works\n")
                self.list_label2.setStyleSheet("""background-color: lightGray;
                                        font-family: Titillium;
                                        font-size: 18px;
                                        border: 4px inset darkGray;
                                        """) 
                self.list_label1.setStyleSheet("""background-color: lightGray;
                                        font-family: Titillium;
                                        font-size: 18px;
                                        border: 4px inset darkGray;
                                        """)
                self.list_label3.setStyleSheet("""background-color: darkGray;
                                        font-family: Titillium;
                                        font-size: 18px;
                                        border: 4px inset black;
                                        """)
                self.list_label5.setStyleSheet("""background-color: lightGray;
                                        font-family: Titillium;
                                        font-size: 18px;
                                        border: 4px inset darkGray;
                                        """)
                self.list_label4.setStyleSheet("""background-color: lightGray;
                                        font-family: Titillium;
                                        font-size: 18px;
                                        border: 4px inset darkGray;
                                        """) 
                temp = self.list_label3.text()
                self.line1.setText(str(temp))   
    def watch_list_4(self,event):
                self.list_label4.setStyleSheet("""background-color: darkGray;
                                        font-family: Titillium;
                                        font-size: 18px;
                                        border: 4px inset black;
                                        """) 
                self.list_label1.setStyleSheet("""background-color: lightGray;
                                        font-family: Titillium;
                                        font-size: 18px;
                                        border: 4px inset darkGray;
                                        """)
                self.list_label3.setStyleSheet("""background-color: lightGray;
                                        font-family: Titillium;
                                        font-size: 18px;
                                        border: 4px inset darkGray;
                                        """)
                self.list_label5.setStyleSheet("""background-color: lightGray;
                                        font-family: Titillium;
                                        font-size: 18px;
                                        border: 4px inset darkGray;
                                        """)
                self.list_label2.setStyleSheet("""background-color: lightGray;
                                        font-family: Titillium;
                                        font-size: 18px;
                                        border: 4px inset darkGray;
                                        """) 
                temp = self.list_label4.text()
                self.line1.setText(str(temp))   
    def watch_list_5(self,event):
                self.list_label5.setStyleSheet("""background-color: darkGray;
                                        font-family: Titillium;
                                        font-size: 18px;
                                        border: 4px inset black;
                                        """) 
                self.list_label1.setStyleSheet("""background-color: lightGray;
                                        font-family: Titillium;
                                        font-size: 18px;
                                        border: 4px inset darkGray;
                                        """)
                self.list_label3.setStyleSheet("""background-color: lightGray;
                                        font-family: Titillium;
                                        font-size: 18px;
                                        border: 4px inset darkGray;
                                        """)
                self.list_label2.setStyleSheet("""background-color: lightGray;
                                        font-family: Titillium;
                                        font-size: 18px;
                                        border: 4px inset darkGray;
                                        """)
                self.list_label4.setStyleSheet("""background-color: lightGray;
                                        font-family: Titillium;
                                        font-size: 18px;
                                        border: 4px inset darkGray;
                                        """) 
                temp = self.list_label5.text()
                self.line1.setText(str(temp))   
    def clicked_line(self,event):
                self.list_label5.setStyleSheet("""background-color: lightGray;
                                        font-family: Titillium;
                                        font-size: 18px;
                                        border: 4px inset black;
                                        """) 
                self.list_label1.setStyleSheet("""background-color: lightGray;
                                        font-family: Titillium;
                                        font-size: 18px;
                                        border: 4px inset darkGray;
                                        """)
                self.list_label3.setStyleSheet("""background-color: lightGray;
                                        font-family: Titillium;
                                        font-size: 18px;
                                        border: 4px inset darkGray;
                                        """)
                self.list_label2.setStyleSheet("""background-color: lightGray;
                                        font-family: Titillium;
                                        font-size: 18px;
                                        border: 4px inset darkGray;
                                        """)
                self.list_label4.setStyleSheet("""background-color: lightGray;
                                        font-family: Titillium;
                                        font-size: 18px;
                                        border: 4px inset darkGray;
                                        """) 




    def add_to_list(self):
                #size of list smaller than 5
                if self.watch_list_length<5:
                        if self.line1.text() not in self.listw:#not inside listw
                                #adds it
                                #sets text in labels and shows it
                                self.list_labels[self.watch_list_length].setText(self.line1.text())
                                self.list_labels[self.watch_list_length].show()
                                #updates the listw
                                self.listw[self.watch_list_length]=self.line1.text()
                                #increases counter
                                self.watch_list_length+=1
                        print(self.listw)
                for i in range(5):
                        print(self.list_labels[i].text())
    def remove_from_list(self):
                if self.watch_list_length>0:
                        if self.line1.text()=='':#if its empty
                        
                                self.list_labels[self.watch_list_length-1].setText('')#deletes item (just hides it)
                                self.list_labels[self.watch_list_length-1].hide()
                                self.listw[self.watch_list_length-1]=''#updates parallel list and counter
                                self.watch_list_length-=1
                        else:
                                #if its empty
                                try:
                                        #finds the place of the item
                                        pos=self.listw.index(self.line1.text())
                                        self.watch_list_length-=1
                                        self.list_labels[pos].setText('')
                                        
                                        self.listw[pos]=''
                                except:
                                       print("cant remove that")
                        #everything that is not empty brings it front
                        for i in range(4):
                                if self.listw[i]=='' and self.listw[i+1]!='':
                                        self.listw[i],self.listw[i+1]=self.listw[i+1],self.listw[i]
                        for i in range(5):
                                self.list_labels[i].setText(self.listw[i])
                                self.list_labels[self.watch_list_length].hide()
                print(self.listw)
                for i in range(5):
                        print(self.list_labels[i].text())
    def save_list(self):
                #saves list localy
                with open(self.doc,"w") as wl:
                        for el in self.listw:
                                wl.write(el+'\n')
                #if e-mail exists stores the watchlist on the spreadsheet
                email_exists=calc_handler.email_exists()
                if email_exists:
                        calc_handler.save_watch_list(self.listw)

    def email_yes_click(self):
        self.email_btn_n.setChecked(False)
        self.email_btn_y.setChecked(True)
        email_exists=calc_handler.email_exists()
        if email_exists:#if e-mail exists
                with open('assets/email.txt','r') as mail:
                        email=mail.readline()#read from the file
                if self.email_line.text()=='':#if there is nothing
                        #sets e-mail in yes
                        calc_handler.yes_send(email,email)
                else:
                        #changes the e-mail both localy and on spreadsheet
                        calc_handler.yes_send(self.email_line.text(),email)
                        with open('assets/email.txt','w') as mail:
                            mail.write(self.email_line.text())
        else:#if e-mail doesn't exists
                if self.email_line.text()=='':#if placeholder is empty does nothing
                        print('give your email')
                else:#saves it localy and creates a new line in spreadsheet
                        with open('assets/email.txt','w') as mail:
                            mail.write(self.email_line.text())
                        calc_handler.yes_send_init()
        

    def email_no_click(self):
            #updates the spreadsheet with 'no'
            calc_handler.no_send()
            self.email_btn_y.setChecked(False)
            if self.email_btn_n.isChecked:
                self.email_btn_n.setChecked(True)
                

    def activate_graph(self):
        
        print("Activating Tab 0...")
        try:
                self.graph_window = Graph()
                toolbar = self.graph_window.addToolBar("Stocks")
                
                stocks = ticker_extractor.get_ticker(self.listw)
                print(stocks)
                
                for stock in stocks:
                        button_action = QAction(stock, self.graph_window)
                        button_action.setStatusTip("This is your button")
                        button_action.triggered.connect(lambda checked, s=stock: self.graph_window.onMyToolBarButtonClick(s))
                        if stock != '\n':
                               toolbar.addAction(button_action)
        except Exception as e:
                print("Error in activate_tab_0:", e)    
        self.graph_but.setChecked(False)
    
    
    
    def easter_egg(self,event):
 
        print("works egg")

           

        self.egg = easter_egg_win()
        

        
                        
          
        
                        
class  easter_egg_win(QMainWindow):
                def __init__(self):
                        super().__init__()
                        self.setWindowTitle("credits")
                        self.resize(480,360)
                        cred_lay = QGridLayout()
                        cred_main_widget = QWidget()

                        cred_label1 = QLabel()
                        pixmap = QPixmap("assets\emj.jpg")
                        cred_label1.setPixmap(pixmap)
                        cred_label1.setScaledContents(True)

                        cred_label2 = QLabel("ΣΑΓΙΑΚΟΣ ΠΕΤΡΟΣ: inf2023185\nΝΑΤΣΟΣ ΝΙΚΟΛΑΣ: inf2023144\nΚΟΥΤΣΟΥΡΗΣ ΕΡΡΙΚΟΣ: inf2023095\nΛΥΜΠΙΤΑΚΗΣ ΓΕΩΡΓΙΟΣ: inf2023111")
                        
                        cred_label3 = QLabel()
                        pixmap2 = QPixmap("assets\ionio.png")
                        cred_label3.setPixmap(pixmap2)
                        
                        cred_lay.addWidget(cred_label1,1,0)
                        cred_lay.addWidget(cred_label2,0,0)
                        cred_lay.addWidget(cred_label3,0,1)

                        cred_main_widget.setLayout(cred_lay)
                        cred_main_widget.setStyleSheet("""
                                                        background-color: rgb(145, 200, 170);
                                                        font-family: Titillium;
                                                        font-size: 22px;
                                                        border: 3px inset black
                                                       """)

                        self.setCentralWidget(cred_main_widget)
                        self.show()                       
                        



        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle("Pythia")  # window title to "Py4"
    MainWindow.setWindowIcon(QtGui.QIcon('Icons/logo-small.ico'))  #  window icon
    MainWindow.show()
    sys.exit(app.exec())
