import os
from PyQt4 import QtGui,QtCore

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_bruteforce_attack_dialog(object):
    def setupUi(self, bruteforce_attack_dialog):
        bruteforce_attack_dialog.setObjectName(_fromUtf8("bruteforce_attack_dialog"))
        bruteforce_attack_dialog.resize(630, 648)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(bruteforce_attack_dialog.sizePolicy().hasHeightForWidth())
        bruteforce_attack_dialog.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        bruteforce_attack_dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/bruteforce.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        bruteforce_attack_dialog.setWindowIcon(icon)
        self.verticalLayout_9 = QtGui.QVBoxLayout(bruteforce_attack_dialog)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        spacerItem = QtGui.QSpacerItem(20, 6, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        spacerItem2 = QtGui.QSpacerItem(20, 95, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.attack_server_label = QtGui.QLabel(bruteforce_attack_dialog)
        self.attack_server_label.setText(_fromUtf8(""))
        self.attack_server_label.setPixmap(QtGui.QPixmap(_fromUtf8("%s/Icons/mysql_logo.ico"%(os.getcwd()))))
        self.attack_server_label.setObjectName(_fromUtf8("attack_server_label"))
        self.horizontalLayout_4.addWidget(self.attack_server_label)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_9.addLayout(self.horizontalLayout_4)
        spacerItem4 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem4)
        self.groupBox = QtGui.QGroupBox(bruteforce_attack_dialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.mysql_radio = QtGui.QRadioButton(self.groupBox)
        self.mysql_radio.setChecked(True)
        self.mysql_radio.setObjectName(_fromUtf8("mysql_radio"))
        self.horizontalLayout_3.addWidget(self.mysql_radio)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.oracle_radio = QtGui.QRadioButton(self.groupBox)
        self.oracle_radio.setObjectName(_fromUtf8("oracle_radio"))
        self.horizontalLayout_3.addWidget(self.oracle_radio)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.postgres_radio = QtGui.QRadioButton(self.groupBox)
        self.postgres_radio.setObjectName(_fromUtf8("postgres_radio"))
        self.horizontalLayout_3.addWidget(self.postgres_radio)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.mssql_radio = QtGui.QRadioButton(self.groupBox)
        self.mssql_radio.setObjectName(_fromUtf8("mssql_radio"))
        self.horizontalLayout_3.addWidget(self.mssql_radio)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_3)
        self.verticalLayout_9.addWidget(self.groupBox)
        spacerItem8 = QtGui.QSpacerItem(20, 8, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_9.addItem(spacerItem8)
        self.groupBox_3 = QtGui.QGroupBox(bruteforce_attack_dialog)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.groupBox_3)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.attck_server_checkbox = QtGui.QCheckBox(self.groupBox_3)
        self.attck_server_checkbox.setObjectName(_fromUtf8("attck_server_checkbox"))
        self.verticalLayout_2.addWidget(self.attck_server_checkbox)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem9)
        self.attack_server_linedit = QtGui.QLineEdit(self.groupBox_3)
        self.attack_server_linedit.setObjectName(_fromUtf8("attack_server_linedit"))
        self.verticalLayout.addWidget(self.attack_server_linedit)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.attack_port_linedit = QtGui.QLineEdit(self.groupBox_3)
        self.attack_port_linedit.setObjectName(_fromUtf8("attack_port_linedit"))
        self.horizontalLayout.addWidget(self.attack_port_linedit)
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        spacerItem10 = QtGui.QSpacerItem(46, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_9.addWidget(self.groupBox_3)
        spacerItem11 = QtGui.QSpacerItem(23, 9, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_9.addItem(spacerItem11)
        self.groupBox_2 = QtGui.QGroupBox(bruteforce_attack_dialog)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.userlist_button = QtGui.QPushButton(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(11)
        sizePolicy.setVerticalStretch(15)
        sizePolicy.setHeightForWidth(self.userlist_button.sizePolicy().hasHeightForWidth())
        self.userlist_button.setSizePolicy(sizePolicy)
        self.userlist_button.setBaseSize(QtCore.QSize(9, 0))
        self.userlist_button.setIconSize(QtCore.QSize(30, 32))
        self.userlist_button.setObjectName(_fromUtf8("userlist_button"))
        self.verticalLayout_7.addWidget(self.userlist_button)
        self.userlist_details = QtGui.QLabel(self.groupBox_2)
        self.userlist_details.setAlignment(QtCore.Qt.AlignCenter)
        self.userlist_details.setObjectName(_fromUtf8("userlist_details"))
        self.verticalLayout_7.addWidget(self.userlist_details)
        self.horizontalLayout_7.addLayout(self.verticalLayout_7)
        self.blank_password_checkbox = QtGui.QCheckBox(self.groupBox_2)
        self.blank_password_checkbox.setObjectName(_fromUtf8("blank_password_checkbox"))
        self.horizontalLayout_7.addWidget(self.blank_password_checkbox)
        spacerItem12 = QtGui.QSpacerItem(0, 81, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.horizontalLayout_7.addItem(spacerItem12)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.wordlist_button = QtGui.QPushButton(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(11)
        sizePolicy.setVerticalStretch(15)
        sizePolicy.setHeightForWidth(self.wordlist_button.sizePolicy().hasHeightForWidth())
        self.wordlist_button.setSizePolicy(sizePolicy)
        self.wordlist_button.setObjectName(_fromUtf8("wordlist_button"))
        self.verticalLayout_6.addWidget(self.wordlist_button)
        self.wordlist_details = QtGui.QLabel(self.groupBox_2)
        self.wordlist_details.setAlignment(QtCore.Qt.AlignCenter)
        self.wordlist_details.setObjectName(_fromUtf8("wordlist_details"))
        self.verticalLayout_6.addWidget(self.wordlist_details)
        self.horizontalLayout_7.addLayout(self.verticalLayout_6)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_7)
        self.verticalLayout_9.addWidget(self.groupBox_2)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        spacerItem13 = QtGui.QSpacerItem(25, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem13)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.current_userlist = QtGui.QLabel(bruteforce_attack_dialog)
        self.current_userlist.setAlignment(QtCore.Qt.AlignCenter)
        self.current_userlist.setObjectName(_fromUtf8("current_userlist"))
        self.horizontalLayout_6.addWidget(self.current_userlist)
        spacerItem14 = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem14)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.progressBar_2 = QtGui.QProgressBar(bruteforce_attack_dialog)
        self.progressBar_2.setObjectName(_fromUtf8("progressBar_2"))
        self.verticalLayout_5.addWidget(self.progressBar_2)
        self.horizontalLayout_9.addLayout(self.verticalLayout_5)
        spacerItem15 = QtGui.QSpacerItem(58, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem15)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.current_password = QtGui.QLabel(bruteforce_attack_dialog)
        self.current_password.setAlignment(QtCore.Qt.AlignCenter)
        self.current_password.setObjectName(_fromUtf8("current_password"))
        self.horizontalLayout_5.addWidget(self.current_password)
        spacerItem16 = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem16)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.progressBar = QtGui.QProgressBar(bruteforce_attack_dialog)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout_4.addWidget(self.progressBar)
        self.horizontalLayout_9.addLayout(self.verticalLayout_4)
        spacerItem17 = QtGui.QSpacerItem(25, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem17)
        self.verticalLayout_9.addLayout(self.horizontalLayout_9)
        spacerItem18 = QtGui.QSpacerItem(27, 15, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_9.addItem(spacerItem18)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.attack_error_label = QtGui.QLabel(bruteforce_attack_dialog)
        self.attack_error_label.setAlignment(QtCore.Qt.AlignCenter)
        self.attack_error_label.setObjectName(_fromUtf8("attack_error_label"))
        self.verticalLayout_8.addWidget(self.attack_error_label)
        spacerItem19 = QtGui.QSpacerItem(23, 5, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_8.addItem(spacerItem19)
        self.attack_status_textBrowser = QtGui.QTextBrowser(bruteforce_attack_dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.attack_status_textBrowser.sizePolicy().hasHeightForWidth())
        self.attack_status_textBrowser.setSizePolicy(sizePolicy)
        self.attack_status_textBrowser.setObjectName(_fromUtf8("attack_status_textBrowser"))
        self.verticalLayout_8.addWidget(self.attack_status_textBrowser)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        spacerItem20 = QtGui.QSpacerItem(158, 37, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem20)
        self.attack_button = QtGui.QPushButton(bruteforce_attack_dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.attack_button.sizePolicy().hasHeightForWidth())
        self.attack_button.setSizePolicy(sizePolicy)
        self.attack_button.setObjectName(_fromUtf8("attack_button"))
        self.horizontalLayout_10.addWidget(self.attack_button)
        spacerItem21 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem21)
        self.stop_attack_button = QtGui.QPushButton(bruteforce_attack_dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.stop_attack_button.sizePolicy().hasHeightForWidth())
        self.stop_attack_button.setSizePolicy(sizePolicy)
        self.stop_attack_button.setObjectName(_fromUtf8("stop_attack_button"))
        self.horizontalLayout_10.addWidget(self.stop_attack_button)
        spacerItem22 = QtGui.QSpacerItem(188, 37, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem22)
        self.verticalLayout_9.addLayout(self.horizontalLayout_10)

        self.retranslateUi(bruteforce_attack_dialog)
        QtCore.QMetaObject.connectSlotsByName(bruteforce_attack_dialog)


    def retranslateUi(self, bruteforce_attack_dialog):
        bruteforce_attack_dialog.setWindowTitle(QtGui.QApplication.translate("bruteforce_attack_dialog", "Database Bruteforce ", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("bruteforce_attack_dialog", "Database Type", None, QtGui.QApplication.UnicodeUTF8))
        self.mysql_radio.setText(QtGui.QApplication.translate("bruteforce_attack_dialog", "MySQL", None, QtGui.QApplication.UnicodeUTF8))
        self.oracle_radio.setText(QtGui.QApplication.translate("bruteforce_attack_dialog", "Oracle", None, QtGui.QApplication.UnicodeUTF8))
        self.postgres_radio.setText(QtGui.QApplication.translate("bruteforce_attack_dialog", "PostgreSQL", None, QtGui.QApplication.UnicodeUTF8))
        self.mssql_radio.setText(QtGui.QApplication.translate("bruteforce_attack_dialog", "MS-SQL", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("bruteforce_attack_dialog", "Database Connection ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("bruteforce_attack_dialog", "MySQL Server:", None, QtGui.QApplication.UnicodeUTF8))
        self.attck_server_checkbox.setText(QtGui.QApplication.translate("bruteforce_attack_dialog", "MySQL Port:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("bruteforce_attack_dialog", "( Default MySQL port is 3306 TCP )", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("bruteforce_attack_dialog", "Dictionary Attack Options", None, QtGui.QApplication.UnicodeUTF8))
        self.userlist_button.setText(QtGui.QApplication.translate("bruteforce_attack_dialog", "User List", None, QtGui.QApplication.UnicodeUTF8))
        self.userlist_details.setText(QtGui.QApplication.translate("bruteforce_attack_dialog", "", None, QtGui.QApplication.UnicodeUTF8))
        self.blank_password_checkbox.setText(QtGui.QApplication.translate("bruteforce_attack_dialog", "Attempt blank password", None, QtGui.QApplication.UnicodeUTF8))
        self.wordlist_button.setText(QtGui.QApplication.translate("bruteforce_attack_dialog", "Word List", None, QtGui.QApplication.UnicodeUTF8))
        self.wordlist_details.setText(QtGui.QApplication.translate("bruteforce_attack_dialog", "", None, QtGui.QApplication.UnicodeUTF8))
        self.stop_attack_button.setText(QtGui.QApplication.translate("bruteforce_attack_dialog", "Stop Attack", None, QtGui.QApplication.UnicodeUTF8))
        self.current_userlist.setText(QtGui.QApplication.translate("bruteforce_attack_dialog", "<font color=red>Not Started</font>", None, QtGui.QApplication.UnicodeUTF8))
        self.current_password.setText(QtGui.QApplication.translate("bruteforce_attack_dialog", "<font color=red>Not Started</font>", None, QtGui.QApplication.UnicodeUTF8))
        self.attack_button.setText(QtGui.QApplication.translate("bruteforce_attack_dialog", "Launch Attack", None, QtGui.QApplication.UnicodeUTF8))
