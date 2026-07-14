import os
import sys
import threading
import urllib.request

import webview

# versão publicada do app; o executável baixa daqui para se manter atualizado
ATUALIZACAO_URL = "https://raw.githubusercontent.com/Bunnyzzx/Moneta/main/index.html"


def resource_path(relative):
    # quando empacotado pelo PyInstaller os arquivos ficam em _MEIPASS
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, relative)


def baixar_atualizacao(destino):
    # baixa a versão mais recente em segundo plano; passa a valer na
    # próxima abertura do app, sem precisar reinstalar o executável
    try:
        with urllib.request.urlopen(ATUALIZACAO_URL, timeout=15) as resposta:
            html = resposta.read()
        if b"</html>" not in html.lower():
            return
        temporario = destino + ".tmp"
        with open(temporario, "wb") as arquivo:
            arquivo.write(html)
        os.replace(temporario, destino)
    except Exception:
        pass  # sem internet ou erro no download: segue com a versão local


def main():
    # guarda o localStorage em %APPDATA%\Moneta para os gastos persistirem
    storage = os.path.join(os.environ.get("APPDATA", "."), "Moneta")
    os.makedirs(storage, exist_ok=True)

    # usa a cópia atualizada (baixada numa execução anterior) se existir;
    # senão, a versão embutida no executável
    atualizado = os.path.join(storage, "index.html")
    pagina = atualizado if os.path.exists(atualizado) else resource_path("index.html")
    threading.Thread(target=baixar_atualizacao, args=(atualizado,), daemon=True).start()

    webview.create_window(
        "Moneta — Controle de Gastos",
        pagina,
        width=860,
        height=900,
        min_size=(420, 600),
    )
    webview.start(private_mode=False, storage_path=storage)


if __name__ == "__main__":
    main()
