import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QListWidget, QListWidgetItem, QVBoxLayout, QWidget, QLabel, QLineEdit, QFormLayout,
    QDialog, QDialogButtonBox ,QHBoxLayout, QCheckBox
)
from PySide6.QtCore import Qt
from ultrasonic_meter_form import UltrasonicMeterForm  
from presenca_liquido import PresencaLiquidoForm


class PressureForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QFormLayout(self)
        
        # Adicione aqui os campos do formulário
        layout.addRow("Entrada (FS-01 ou FS-02):", QLineEdit())
        layout.addRow("PT-200 (Psig):", QLineEdit())
        layout.addRow("PT-400 (Psig):", QLineEdit())
        layout.addRow("SamplerGC (Psig):", QLineEdit())
        layout.addRow("PI 307 MTGÁS (Psig):", QLineEdit())
        layout.addRow("Cilindro de Gás Padrão (Psig):", QLineEdit())
        layout.addRow("FS-03 Entrada (Psig):", QLineEdit())
        layout.addRow("FS-03 Saida (Psig):", QLineEdit())
        layout.addRow("V-100 (Psig):", QLineEdit())
        
        # adicona check list na mlv-27
        mlv_layout = QHBoxLayout()
        mlv_checkbox1 = QCheckBox("ABERTA")
        mlv_checkbox2 = QCheckBox("FECHADA")
        mlv_layout.addWidget(mlv_checkbox1)
        mlv_layout.addWidget(mlv_checkbox2)
        layout.addRow("MLV-27 (Psig):", mlv_layout)
        
        # Continue adicionando os campos necessários...

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Layout principal
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Menu lateral
        self.sidebar = QListWidget()
        self.sidebar.setFixedWidth(200)
        
        # Adicionando itens ao menu lateral
        self.add_sidebar_item("Dashboard")
        self.add_sidebar_item("PRESSÕES")
        self.sidebar.addItem("MEDIDOR ULTRASSONICO/MU")
        self.sidebar.addItem("PRESENÇA DE LÍQUIDOS")
        self.sidebar.addItem("ESD")
        self.sidebar.addItem("GÁS HÉLIO AMOSTRAGEM")
        self.sidebar.addItem("PRESENÇA DE LÍQUIDOS")
        self.sidebar.addItem("RAMAIS")
        self.sidebar.addItem("EQUIPAMENTOS")
        self.sidebar.addItem("APR / AGGREKO")
        # Adicione os outros itens aqui...

        self.layout.addWidget(self.sidebar, alignment=Qt.AlignLeft)

        # Conectar o sinal itemClicked ao método de tratamento
        self.sidebar.itemClicked.connect(self.on_item_clicked)

        # Área do dashboard
        self.dashboard_label = QLabel("Gasocidente")
        self.dashboard_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.dashboard_label, alignment=Qt.AlignCenter)

        # Estilização
        self.setup_styles()

        # Configurações da janela
        self.setWindowTitle('Formulario de Campo')
        self.setGeometry(300, 300, 800, 600)
    
    def add_sidebar_item(self, name):
        item = QListWidgetItem(name)
        self.sidebar.addItem(item)
        
    def on_item_clicked(self, item):
        if item.text() == "PRESSÕES":
            self.show_pressure_form()
        elif item.text() == "MEDIDOR ULTRASSONICO/MU":
            self.show_ultrasonic_meter_form()
        elif item.text() == "PRESENÇA DE LÍQUIDOS":
            self.show_PresencaLiquidoForm()
            
            
    def show_PresencaLiquidoForm(self):
        # Aqui você cria o formulário e o define como modal
        form_dialog = PressureForm(self)
        form_dialog.exec_()        
                
    def show_pressure_form(self):
        # Aqui você cria o formulário e o define como modal
        form_dialog = PressureForm(self)
        form_dialog.exec_()        

        
    def show_ultrasonic_meter_form(self):
       form_dialog = UltrasonicMeterForm(self)
       form_dialog.exec_()

    def setup_styles(self):
        self.setStyleSheet("""
            QListWidget {
                background-color: #008000;
                color: white;
            }
            QListWidget::item:selected {
                background-color: #007fff;
            }
            QLabel {
                font-size: 24px;
            }
        """)

# Inicialização da aplicação
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
