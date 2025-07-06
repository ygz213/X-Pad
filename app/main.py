from os import path
from sys import argv
from PyQt6 import QtCore, QtGui, QtWidgets



class XPad(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('X-Pad')
        self.setWindowIcon(QtGui.QIcon(f'{path.join(path.dirname(argv[0]))}/icons/icon.png'))

        self.menu_bar = QtWidgets.QMenuBar(self)
        self.menu_bar.addMenu('Settings')
        self.setMenuBar(self.menu_bar)
        miscellaneous = self.menu_bar.addMenu('Miscellaneous')
        miscellaneous.addAction('GitHub repository')
        miscellaneous.addAction('License')
        self.draw_widgets()


    def draw_widgets(self):
        main_frame = QtWidgets.QWidget(self)
        self.setCentralWidget(main_frame)
        main_layout = QtWidgets.QGridLayout(main_frame)
        main_frame.setLayout(main_layout)

        self.notes = QtWidgets.QTreeWidget(self)
        self.notes.setHeaderHidden(True)
        self.notes.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.notes.customContextMenuRequested.connect(self.show_context_menu)
        main_layout.addWidget(self.notes)

        button_layout = QtWidgets.QVBoxLayout()

        self.new_note = QtWidgets.QPushButton('     New note...', self)
        self.new_note.setIcon(QtGui.QIcon(f'{path.join(path.dirname(argv[0]))}/icons/new_note.png'))
        self.new_note.setIconSize(QtCore.QSize(20, 20))
        self.new_note.setFixedHeight(35)
        self.new_note.setFixedWidth(125)
        button_layout.addWidget(self.new_note)

        self.new_folder = QtWidgets.QPushButton('     New folder...', self)
        self.new_folder.setIcon(QtGui.QIcon(f'{path.join(path.dirname(argv[0]))}/icons/new_folder.png'))
        self.new_folder.setIconSize(QtCore.QSize(20, 20))
        self.new_folder.setFixedHeight(35)
        self.new_folder.setFixedWidth(125)
        button_layout.addWidget(self.new_folder)

        buttons_frame = QtWidgets.QWidget(self)
        buttons_frame.setLayout(button_layout)
        main_layout.addWidget(buttons_frame, 0, 1, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)

        self.showMaximized()



    def show_context_menu(self, position):
        context_menu = QtWidgets.QMenu(self)

        edit_action = QtGui.QAction('Edit...', self)
        #edit_action.triggered.connect()
        context_menu.addAction(edit_action)

        delete_action = QtGui.QAction('Remove...', self)
        #delete_action.triggered.connect()
        context_menu.addAction(delete_action)
        context_menu.exec(self.notes.viewport().mapToGlobal(position))



application = QtWidgets.QApplication(argv)
window = XPad()
window.show()
application.exec()