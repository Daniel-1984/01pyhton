from PySide6.QtWidgets import QDialog, QFormLayout, QDialogButtonBox, QComboBox, QLineEdit

class UltrasonicMeterForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QFormLayout(self)
        
        # Adicione aqui os campos do formulário
        layout.addRow("FT-200 condições:", QComboBox())
        layout.addRow("FT-400 condições:", QComboBox())
        layout.addRow("Pressão de Líquido:", QLineEdit())
        layout.addRow("FS-01 condição :", QComboBox())
        layout.addRow("FS-02 condição:", QComboBox())
        layout.addRow("Pressão Dif. Filt. em Op.:", QLineEdit())
        layout.addRow("FS-03 condição:", QComboBox())
        layout.addRow("V-100:", QComboBox())

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)