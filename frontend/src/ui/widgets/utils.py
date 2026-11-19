from PySide6.QtWidgets import QWidget, QVBoxLayout


def embed_widget(container: QWidget, child: QWidget, margin: int = 2) -> None:
    layout = container.layout()
    if layout is None:
        layout = QVBoxLayout(container)
    layout.setContentsMargins(margin, margin, margin, margin)
    layout.addWidget(child)