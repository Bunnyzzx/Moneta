import os
import sys

import webview


def resource_path(relative):
    # quando empacotado pelo PyInstaller os arquivos ficam em _MEIPASS
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, relative)


def main():
    # guarda o localStorage em %APPDATA%\Moneta para os gastos persistirem
    storage = os.path.join(os.environ.get("APPDATA", "."), "Moneta")
    os.makedirs(storage, exist_ok=True)

    webview.create_window(
        "Moneta — Controle de Gastos",
        resource_path("index.html"),
        width=860,
        height=900,
        min_size=(420, 600),
    )
    webview.start(private_mode=False, storage_path=storage)


if __name__ == "__main__":
    main()
