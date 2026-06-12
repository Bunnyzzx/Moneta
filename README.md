# 💸 Moneta

Aplicativo de controle de gastos pessoais — simples, bonito e sem complicação.
Feito em HTML, CSS e JavaScript puros: basta abrir o `index.html` no navegador, sem instalar nada.

## ✨ Funcionalidades

- **Registro rápido de gastos** — nome e valor (aceita `60,50`, `60.50` ou `R$ 60,50`)
- **Gastos essenciais** — marque aluguel, luz, água etc. com o selo "essencial"
- **Gastos fixos** — lançou uma vez, aparece automaticamente em todos os meses seguintes
- **Navegação por mês** — seletor "Mês" para ver o histórico completo; nada é apagado na virada do mês
- **Saldo disponível por mês** — defina quanto você tem para gastar em cada mês
- **Ainda disponível** — quanto sobra no mês (verde) ou quanto estourou (vermelho)
- **Restante total** — acumulado das sobras de todos os meses
- **Gráficos** — barras com os maiores gastos do mês e rosca de essencial × não essencial
- **Edição completa** — altere nome, valor e marcações de qualquer gasto depois de lançado
- **Dados persistentes** — tudo fica salvo no navegador (localStorage)

## 📥 Download (Windows)

A forma mais fácil de usar o Moneta:

1. Acesse a [página de releases](https://github.com/Bunnyzzx/Moneta/releases/latest)
2. Baixe o arquivo **`Moneta.exe`**
3. Dê dois cliques para abrir — **não precisa instalar nada**

> ⚠️ Na primeira execução o Windows pode mostrar o aviso "SmartScreen" por ser um app novo.
> Clique em **"Mais informações" → "Executar assim mesmo"**.

Seus gastos ficam salvos no computador (em `%APPDATA%\Moneta`) e **não são perdidos ao fechar o app**.

## 🚀 Como usar no navegador

1. Baixe ou clone o repositório:
   ```bash
   git clone https://github.com/Bunnyzzx/Moneta.git
   ```
2. Abra o arquivo `index.html` no navegador. Pronto!

### 🖥️ Versão desktop (Windows)

Para gerar um executável (`Moneta.exe`) com janela própria:

```bash
pip install pywebview pyinstaller
pyinstaller --noconfirm --onefile --windowed --name Moneta --add-data "index.html;." app.py
```

O executável fica em `dist/Moneta.exe`. Os dados são salvos em `%APPDATA%\Moneta` e **persistem entre as aberturas do app**.

## 🛠️ Tecnologias

- HTML5
- CSS3 (tema escuro com gradientes)
- JavaScript vanilla (sem frameworks nem dependências)
