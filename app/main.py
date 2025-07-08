from os import path, startfile
from subprocess import call
from sys import argv, platform
from webbrowser import open_new_tab
from PyQt6 import QtCore, QtGui, QtWidgets



def open_license_file():
    if platform == 'win32':
        startfile(f'{path.join(path.dirname(argv[0]))[:-4]}/LICENSE')
    elif platform == 'darwin':
        call(['open', f'{path.join(path.dirname(argv[0]))[:-4]}/LICENSE'])
    else:
        call(['xdg-open', f'{path.join(path.dirname(argv[0]))[:-4]}/LICENSE'])


class XPad(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('X-Pad')
        self.setWindowIcon(QtGui.QIcon(f'{path.join(path.dirname(argv[0]))}/icons/icon.png'))

        menu_bar = QtWidgets.QMenuBar(self)
        menu_bar.addMenu('Settings')
        self.setMenuBar(menu_bar)
        miscellaneous = menu_bar.addMenu('Miscellaneous')
        miscellaneous.addAction('GitHub repository', lambda: open_new_tab('https://github.com/ygz213/X-Pad'))
        miscellaneous.addAction('License', lambda: open_license_file())
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

        new_note = QtWidgets.QPushButton('     New note...', self)
        new_note.setIcon(QtGui.QIcon(f'{path.join(path.dirname(argv[0]))}/icons/new_note.png'))
        new_note.setIconSize(QtCore.QSize(20, 20))
        new_note.setFixedHeight(35)
        new_note.setFixedWidth(125)
        button_layout.addWidget(new_note)

        new_folder = QtWidgets.QPushButton('     New folder...', self)
        new_folder.setIcon(QtGui.QIcon(f'{path.join(path.dirname(argv[0]))}/icons/new_folder.png'))
        new_folder.setIconSize(QtCore.QSize(20, 20))
        new_folder.setFixedHeight(35)
        new_folder.setFixedWidth(125)
        button_layout.addWidget(new_folder)

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