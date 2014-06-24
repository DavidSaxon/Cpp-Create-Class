#!/usr/bin/env python

import sys
from PyQt4 import QtCore, QtGui

#-------------------------------------------------------------------------------
#                                 GLOBAL VARIABLES
#-------------------------------------------------------------------------------

#style sheets
style_sheet_title    = "font-size: 10pt; font-family: San-Serif;"
style_sheet_text     = "font-size: 10pt; font-family: San-Serif;"
style_sheet_required = "font-size: 10pt; font-family: San-Serif; color: red"
style_sheet_button   = "font-size: 10pt; font-family: San-Serif;"

#includes list
includes = []
#namespace list
namespaces = []

#-------------------------------------------------------------------------------
#                              ADDABLE TEXT BOX CLASS
#-------------------------------------------------------------------------------

class AddText():

    #---------------------------------------------------------------------------
    #                                 CONSTRUCTOR
    #---------------------------------------------------------------------------

    def __init__(self, qt, layout, list):

        self.parent = qt
        self.parent_layout = layout
        self.text_list = list

        self.text = QtGui.QLineEdit(self.parent)
        self.text.setStyleSheet(style_sheet_text)

        self.remove_button = QtGui.QPushButton("-", self.parent)
        self.remove_button.setStyleSheet(style_sheet_button)
        self.remove_button.clicked.connect(self._remove)

        self.line_layout = QtGui.QHBoxLayout()
        self.line_layout.addWidget(self.text)
        self.line_layout.addWidget(self.remove_button)
        self.parent_layout.addLayout(self.line_layout)

        self.text.setFocus()

        self.text_list.append(self)


    #---------------------------------------------------------------------------
    #                               PUBLIC METHODS
    #---------------------------------------------------------------------------

    def get_text(self):

        return self.text.text()

    #---------------------------------------------------------------------------
    #                               PRIVATE METHODS
    #---------------------------------------------------------------------------

    #remove the text
    def _remove(self):

        self.text_list.remove(self)
        self.text.setParent(None)
        self.remove_button.setParent(None)
        self.line_layout.setParent(None)

#-------------------------------------------------------------------------------
#                          ADDABLE DOUBLE TEXT BOX CLASS
#-------------------------------------------------------------------------------

class AddDoubleText():

    #---------------------------------------------------------------------------
    #                                 CONSTRUCTOR
    #---------------------------------------------------------------------------

    def __init__(self, qt, layout, list):

        self.parent = qt
        self.parent_layout = layout
        self.text_list = list

        self.comment = QtGui.QLabel(self.parent)
        self.comment.setStyleSheet(style_sheet_title)
        self.comment.setText("    Comment:")
        self.comment.adjustSize()

        self.first_text = QtGui.QLineEdit(self.parent)
        self.first_text.setStyleSheet(style_sheet_text)

        self.name = QtGui.QLabel(self.parent)
        self.name.setStyleSheet(style_sheet_title)
        self.name.setText("    Name: ")
        self.name.adjustSize()

        self.second_text = QtGui.QLineEdit(self.parent)
        self.second_text.setStyleSheet(style_sheet_text)

        self.remove_button = QtGui.QPushButton("-", self.parent)
        self.remove_button.setStyleSheet(style_sheet_button)
        self.remove_button.clicked.connect(self._remove)

        self.first_layout = QtGui.QHBoxLayout()
        self.first_layout.addWidget(self.comment)
        self.first_layout.addWidget(self.first_text)
        self.second_layout = QtGui.QHBoxLayout()
        self.second_layout.addWidget(self.name)
        self.second_layout.addWidget(self.second_text)

        self.inner_layout = QtGui.QVBoxLayout()
        self.inner_layout.addLayout(self.first_layout)
        self.inner_layout.addLayout(self.second_layout)

        self.line_layout = QtGui.QHBoxLayout()
        self.line_layout.addLayout(self.inner_layout)
        self.line_layout.addWidget(self.remove_button)

        self.parent_layout.addLayout(self.line_layout)

        self.line = QtGui.QFrame()
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.parent_layout.addWidget(self.line)

        self.second_text.setFocus()

        self.text_list.append(self)


    #---------------------------------------------------------------------------
    #                               PUBLIC METHODS
    #---------------------------------------------------------------------------

    def get_first_text(self):

        return self.first_text.text()


    def get_second_text(self):

        return self.second_text.text()

    #---------------------------------------------------------------------------
    #                               PRIVATE METHODS
    #---------------------------------------------------------------------------

    #remove the text
    def _remove(self):

        self.text_list.remove(self)

        self.comment.setParent(None)
        self.first_text.setParent(None)
        self.first_layout.setParent(None)
        self.name.setParent(None)
        self.second_text.setParent(None)
        self.second_layout.setParent(None)
        self.inner_layout.setParent(None)
        self.remove_button.setParent(None)
        self.line.setParent(None)

#-------------------------------------------------------------------------------
#                                    MAIN CLASS
#-------------------------------------------------------------------------------

class CreateSourceHeaderClass(QtGui.QWidget):

    #---------------------------------------------------------------------------
    #                                 VARIABLES
    #---------------------------------------------------------------------------

    #dimensions
    indentation = 30
    text_height = 30
    height = 0

    #dets
    source_path   = ""
    header_path   = ""
    file_name     = ""
    class_name    = ""
    extends       = ""
    class_comment = ""
    include_guard = ""

    #---------------------------------------------------------------------------
    #                                 CONSTRUCTOR
    #---------------------------------------------------------------------------

    #sets up the file maker
    def __init__(self, parent = None):

        # QtGui.QWidget.__init__(self)

        super(CreateSourceHeaderClass, self).__init__()

        self._initUI()


    #---------------------------------------------------------------------------
    #                              PRIVATE METHODS
    #---------------------------------------------------------------------------

    #when the source path changes
    def _source_path_change(self, text):

        original_text = self.source_path

        self.source_path = text
        self.source_path_required.setText("")

        if self.header_path == "" or self.header_path == original_text:
            self.header_path = text
            self.header_path_text.setText(text)


    #when the source path browser button is pressed
    def _source_path_browser(self):

        self.source_path_text.setText(QtGui.QFileDialog.getExistingDirectory())


    #when the header path changes
    def _header_path_change(self, text):

        self.header_path = text
        self.header_path_required.setText("")


    #when the header path browser button is pressed
    def _header_path_browser(self):

        self.header_path_text.setText(QtGui.QFileDialog.getExistingDirectory())


    #when the file name entered changes
    def _file_name_change(self, text):

        original_text = self.file_name

        if self.class_name == "" or self.class_name == original_text:
            self.class_name = text
            self.class_name_text.setText(text)

        self.file_name = text
        self.file_name_required.setText("")


    #when the class name entered changes
    def _class_name_change(self, text):

        self.class_name = text
        self.class_name_required.setText("")


    #when the extends entered changes
    def _extends_change(self, text):

        self.extends = text


    #when the class comment entered changes
    def _class_comment_change(self, text):

        self.class_comment = text


    #when the include guard entered changes
    def _include_guard_change(self, text):

        self.include_guard = text


    #when the add include button is pressed
    def _add_include(self):

        AddText(self, self.include_layout, includes)


    #when the add namespace button is pressed
    def _add_namespace(self):

        AddDoubleText(self, self.namespace_layout, namespaces)


    #when the done button is pressed
    def _done_button(self):

        #check the required attributes
        checkFailed = False
        if self.source_path == "":
            self.source_path_required.setText("Required")
            checkFailed = True
        if self.header_path == "":
            self.header_path_required.setText("Required")
            checkFailed = True
        if self.file_name == "":
            self.file_name_required.setText("Required")
            checkFailed = True
        if self.class_name == "":
            self.class_name_required.setText("Required")
            checkFailed = True

        if checkFailed:
            return

        #create files
        self._create_source()
        self._create_header()

        #exit
        QtGui.QApplication.quit()


    #when the cancel button is pressed
    def _cancel_button(self):

        #exit
        QtGui.QApplication.quit()


    #creates the source file
    def _create_source(self):

        source = open(self.source_path + "/" + self.file_name + ".cpp", "w")

        source.write("//TODO: #include")

        self._write_namespace_begin(False, source)

        self._write_namespace_ends(source)


    #creates the source file
    def _create_header(self):

        header = open(self.header_path + "/" + self.file_name + ".hpp", "w")

        if self.include_guard != "":
            header.write("#ifndef " + self.include_guard + "\n")
            header.write("#    define " + self.include_guard + "\n" + "\n")

        for include in includes:
            if include != "":
                header.write("#include " + include.get_text() + "\n")

        if len(includes) > 0:
            header.write("\n")

        self._write_namespace_begin(True, header)

        if self.class_comment != "":
            header.write(self._box_comment(str(self.class_comment)) + "\n")

        header.write("class " + self.class_name)
        if self.extends != "":
            header.write(" : " + self.extends)
        header.write("  {\n\n")

        header.write("};\n\n")

        self._write_namespace_ends(header)

        if self.include_guard != "":
            header.write("\n#endif")

        header.write("\n")


    #writes namespace begins to a file
    def _write_namespace_begin(self, comment, file):

        for namespace in namespaces:
            if namespace != "":
                if comment and namespace.get_first_text() != "":
                    file.write(self._box_comment(
                        namespace.get_first_text()) + "\n")
                file.write(namespace.get_second_text() + " {\n\n")


    #write the namespace ends to a file
    def _write_namespace_ends(self, file):

        for namespace in namespaces:
            if namespace != "":
                file.write("} //" + "namespace " +
                    namespace.get_second_text() + "\n\n")


    #creates a box comment
    def _box_comment(self, text):

        #split the string into lines
        lines = []
        longest_line = -1
        while len(text) > 76:

            column = 0
            #find the first white space less than 76 characters
            for i in reversed(range(77)):
                if text[i] == " ":
                    column = i
                    break

            if column > 0:
                lines.append(text[ : column])
                text = text[column + 1: ]

            if column > longest_line:
                longest_line = column

        if longest_line < 0:
            longest_line = len(text)

        if len(text) > 0:
            lines.append(text)

        #generate stars
        stars = "*" * (longest_line + 2)

        #make the comment
        comment = "/" + stars + "\\\n"
        for line in lines:
            line += " " * (longest_line - len(line))
            comment += "| " + line + " |\n"
        comment += "\\" + stars + "/"

        return comment

    #INCOMING WALL OF TEXT
    #set up the ui elements.
    def _initUI(self):

        self.layout = QtGui.QVBoxLayout()

        divider1 = QtGui.QFrame()
        divider1.setFrameShape(QtGui.QFrame.HLine)
        self.layout.addWidget(divider1)

        #source path
        source_path_title = QtGui.QLabel(self)
        source_path_title.setStyleSheet(style_sheet_title)
        source_path_title.setText("Source Folder Path:")
        source_path_title.adjustSize()
        self.layout.addWidget(source_path_title)

        self.source_path_text = QtGui.QLineEdit(self)
        self.source_path_text.setStyleSheet(style_sheet_text)
        self.source_path_text.textChanged[str].connect(self._source_path_change)

        source_path_browser = QtGui.QPushButton("...", self)
        source_path_browser.setStyleSheet(style_sheet_button)
        source_path_browser.clicked.connect(self._source_path_browser)

        self.source_path_required = QtGui.QLabel(self)
        self.source_path_required.setStyleSheet(style_sheet_required)
        self.source_path_required.setText("Required")
        self.source_path_required.adjustSize()
        self.source_path_required.setText("")
        self.source_path_required.adjustSize()

        source_path_layout = QtGui.QHBoxLayout()
        source_path_layout.addWidget(self.source_path_text)
        source_path_layout.addWidget(source_path_browser)
        source_path_layout.addWidget(self.source_path_required)
        self.layout.addLayout(source_path_layout)

        #header path
        header_path_title = QtGui.QLabel(self)
        header_path_title.setStyleSheet(style_sheet_title)
        header_path_title.setText("Header Folder Path:")
        header_path_title.adjustSize()
        self.layout.addWidget(header_path_title)

        self.header_path_text = QtGui.QLineEdit(self)
        self.header_path_text.setStyleSheet(style_sheet_text)
        self.header_path_text.textChanged[str].connect(self._header_path_change)

        header_path_browser = QtGui.QPushButton("...", self)
        header_path_browser.setStyleSheet(style_sheet_button)
        header_path_browser.clicked.connect(self._header_path_browser)

        self.header_path_required = QtGui.QLabel(self)
        self.header_path_required.setStyleSheet(style_sheet_required)
        self.header_path_required.setText("Required")
        self.header_path_required.adjustSize()
        self.header_path_required.setText("")
        self.header_path_required.adjustSize()

        header_path_layout = QtGui.QHBoxLayout()
        header_path_layout.addWidget(self.header_path_text)
        header_path_layout.addWidget(header_path_browser)
        header_path_layout.addWidget(self.header_path_required)
        self.layout.addLayout(header_path_layout)

        divider2 = QtGui.QFrame()
        divider2.setFrameShape(QtGui.QFrame.HLine)
        self.layout.addWidget(divider2)

        #the name of the file
        file_name_title = QtGui.QLabel(self)
        file_name_title.setStyleSheet(style_sheet_title)
        file_name_title.setText("File Name (Do not include extension):")
        file_name_title.adjustSize()
        self.layout.addWidget(file_name_title)

        file_name_text = QtGui.QLineEdit(self)
        file_name_text.setStyleSheet(style_sheet_text)
        file_name_text.textChanged[str].connect(self._file_name_change)

        self.file_name_required = QtGui.QLabel(self)
        self.file_name_required.setStyleSheet(style_sheet_required)
        self.file_name_required.setText("Required")
        self.file_name_required.adjustSize()
        self.file_name_required.setText("")
        self.file_name_required.adjustSize()

        file_name_layout = QtGui.QHBoxLayout()
        file_name_layout.addWidget(file_name_text)
        file_name_layout.addWidget(self.file_name_required)
        self.layout.addLayout(file_name_layout)

        #the name of the class
        class_name_title = QtGui.QLabel(self)
        class_name_title.setStyleSheet(style_sheet_title)
        class_name_title.setText("Class Name:")
        class_name_title.adjustSize()
        self.layout.addWidget(class_name_title)

        self.class_name_text = QtGui.QLineEdit(self)
        self.class_name_text.setStyleSheet(style_sheet_text)
        self.class_name_text.textChanged[str].connect(self._class_name_change)

        self.class_name_required = QtGui.QLabel(self)
        self.class_name_required.setStyleSheet(style_sheet_required)
        self.class_name_required.setText("Required")
        self.class_name_required.adjustSize()
        self.class_name_required.setText("")
        self.class_name_required.adjustSize()

        class_name_layout = QtGui.QHBoxLayout()
        class_name_layout.addWidget(self.class_name_text)
        class_name_layout.addWidget(self.class_name_required)
        self.layout.addLayout(class_name_layout)

        #the extends
        extends_title = QtGui.QLabel(self)
        extends_title.setStyleSheet(style_sheet_title)
        extends_title.setText("Extends:")
        extends_title.adjustSize()
        self.layout.addWidget(extends_title)

        extend_text = QtGui.QLineEdit(self)
        extend_text.setStyleSheet(style_sheet_text)
        extend_text.textChanged[str].connect(self._extends_change)
        self.layout.addWidget(extend_text)

        #the class comment
        class_comment_title = QtGui.QLabel(self)
        class_comment_title.setStyleSheet(style_sheet_title)
        class_comment_title.setText("Class Comment:")
        class_comment_title.adjustSize()
        self.layout.addWidget(class_comment_title)

        class_comment_text = QtGui.QLineEdit(self)
        class_comment_text.setStyleSheet(style_sheet_text)
        class_comment_text.textChanged[str].connect(self._class_comment_change)
        self.layout.addWidget(class_comment_text)

        divider2 = QtGui.QFrame()
        divider2.setFrameShape(QtGui.QFrame.HLine)
        self.layout.addWidget(divider2)

        #the include guard
        include_guard_title = QtGui.QLabel(self)
        include_guard_title.setStyleSheet(style_sheet_title)
        include_guard_title.setText("Include Guard:")
        include_guard_title.adjustSize()
        self.layout.addWidget(include_guard_title)

        include_guard_text = QtGui.QLineEdit(self)
        include_guard_text.setStyleSheet(style_sheet_text)
        include_guard_text.textChanged[str].connect(self._include_guard_change)
        self.layout.addWidget(include_guard_text)

        divider3 = QtGui.QFrame()
        divider3.setFrameShape(QtGui.QFrame.HLine)
        self.layout.addWidget(divider3)

        #includes
        include_title = QtGui.QLabel(self)
        include_title.setStyleSheet(style_sheet_title)
        include_title.setText("Includes:")
        include_title.adjustSize()
        self.layout.addWidget(include_title)

        divider4 = QtGui.QFrame()
        divider4.setFrameShape(QtGui.QFrame.HLine)
        self.layout.addWidget(divider4)

        self.include_layout = QtGui.QVBoxLayout()
        self.layout.addLayout(self.include_layout)

        include_button = QtGui.QPushButton("+", self)
        include_button.setStyleSheet(style_sheet_button)
        include_button.clicked.connect(self._add_include)
        include_button_layout = QtGui.QHBoxLayout()
        include_button_layout.addWidget(include_button)
        include_button_layout.addStretch(1)
        self.layout.addLayout(include_button_layout)

        divider5 = QtGui.QFrame()
        divider5.setFrameShape(QtGui.QFrame.HLine)
        self.layout.addWidget(divider5)

        #the namespaces
        namespaces_title = QtGui.QLabel(self)
        namespaces_title.setStyleSheet(style_sheet_title)
        namespaces_title.setText("Namespaces:")
        namespaces_title.adjustSize()
        self.layout.addWidget(namespaces_title)

        divider6 = QtGui.QFrame()
        divider6.setFrameShape(QtGui.QFrame.HLine)
        self.layout.addWidget(divider6)

        self.namespace_layout = QtGui.QVBoxLayout()
        self.layout.addLayout(self.namespace_layout)

        namespace_button = QtGui.QPushButton("+", self)
        namespace_button.setStyleSheet(style_sheet_button)
        namespace_button.clicked.connect(self._add_namespace)
        namespace_button_layout = QtGui.QHBoxLayout()
        namespace_button_layout.addWidget(namespace_button)
        namespace_button_layout.addStretch(1)
        self.layout.addLayout(namespace_button_layout)

        divider7 = QtGui.QFrame()
        divider7.setFrameShape(QtGui.QFrame.HLine)
        self.layout.addWidget(divider7)

        #done button
        done_button = QtGui.QPushButton("Done", self)
        done_button.setStyleSheet(style_sheet_button)
        done_button.clicked.connect(self._done_button)

        #cancel button
        cancel_button = QtGui.QPushButton("Cancel", self)
        cancel_button.setStyleSheet(style_sheet_button)
        cancel_button.clicked.connect(self._cancel_button)

        #buttons
        button_layout = QtGui.QHBoxLayout()
        button_layout.addStretch(1)
        button_layout.addWidget(done_button)
        button_layout.addWidget(cancel_button)
        button_layout.addStretch(1)
        self.layout.addStretch(1)
        self.layout.addLayout(button_layout)

        self.setLayout(self.layout)

        #set up the window
        self.setGeometry(200, 100, 600, 600)
        self.setWindowTitle("Create Source Header Pair")
        self.show()


#-------------------------------------------------------------------------------
#                                       MAIN
#-------------------------------------------------------------------------------

if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    file_maker = CreateSourceHeaderClass()
    #file_maker.show()
    sys.exit(app.exec_())
