# Form implementation generated from reading ui file 'E:\Ml_in_BA\Final\MlInBA_FinalProject\View\UI\DashboardDetailPage.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets

from Service.KPICardService import KPICard, KPIData


class Ui_DashboardDetailPage(object):
    def setupUi(self, WizardPage):
        WizardPage.setObjectName("WizardPage")
        WizardPage.resize(1060, 500)
        self.gridLayout = QtWidgets.QGridLayout(WizardPage)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_kpis_03 = KPICard(KPIData(value=50, unit="Total Quantity", icon_path=""))
        self.frame_kpis_03.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_kpis_03.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_kpis_03.setObjectName("frame_kpis_03")
        self.gridLayout_2.addWidget(self.frame_kpis_03, 0, 2, 1, 1)
        self.frame_kpis_01 = KPICard(KPIData(value=50, unit="Total Sales (USD)", icon_path=""))
        self.frame_kpis_01.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_kpis_01.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_kpis_01.setObjectName("frame_kpis_01")
        self.gridLayout_2.addWidget(self.frame_kpis_01, 0, 0, 1, 1)
        self.frame_kpis_02 = KPICard(KPIData(value=50, unit="Nmber of Order", icon_path=""))
        self.frame_kpis_02.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_kpis_02.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_kpis_02.setObjectName("frame_kpis_02")
        self.gridLayout_2.addWidget(self.frame_kpis_02, 0, 1, 1, 1)
        self.frame_kpis_04 = KPICard(KPIData(value=50, unit="Fulfillment Rate %", icon_path=""))
        self.frame_kpis_04.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_kpis_04.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_kpis_04.setObjectName("frame_kpis_04")
        self.gridLayout_2.addWidget(self.frame_kpis_04, 0, 3, 1, 1)
        self.frame_sales_overview = QtWidgets.QFrame(parent=WizardPage)
        self.frame_sales_overview.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_sales_overview.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_sales_overview.setObjectName("frame_sales_overview")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.frame_sales_overview)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 40, 401, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_visualize = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_visualize.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_visualize.setObjectName("verticalLayout_visualize")
        self.TableView = QtWidgets.QTableView(parent=self.frame_sales_overview)
        self.TableView.setGeometry(QtCore.QRect(570, 40, 401, 281))
        self.TableView.setObjectName("TableView")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.frame_sales_overview)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(570, 10, 401, 23))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(parent=self.horizontalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.horizontalLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout.addWidget(self.comboBox_2)
        self.gridLayout_2.addWidget(self.frame_sales_overview, 1, 0, 3, 4)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 1, 1, 1)

        self.retranslateUi(WizardPage)
        QtCore.QMetaObject.connectSlotsByName(WizardPage)

    def retranslateUi(self, WizardPage):
        _translate = QtCore.QCoreApplication.translate
        WizardPage.setWindowTitle(_translate("WizardPage", "WizardPage"))
        self.label.setText(_translate("WizardPage", "Year"))
        self.label_2.setText(_translate("WizardPage", "Quarter"))