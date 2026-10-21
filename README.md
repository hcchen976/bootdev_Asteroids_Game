SETUP:
這是一份你可以保存起來的筆記，方便日後使用 uv 快速建立 Python + Pygame 專案：

Python + Pygame 專案環境建置指南
1. 建立專案
建立新資料夾並指定 Python 版本（因為 Pygame 尚未支援 Python 3.14，建議使用 3.13）：

uv init --no-package --python 3.13 my-project-name
cd my-project-name

2. 設定虛擬環境 (Virtual Environment)
建立並啟動獨立的虛擬環境，用來隔離專案套件：

# 建立虛擬環境
uv venv

# 啟動虛擬環境 (macOS / Linux):
source .venv/bin/activate

# 啟動虛擬環境 (Windows Git Bash):
source .venv/Scripts/activate

# 啟動虛擬環境 (Windows PowerShell):
.venv\Scripts\Activate.ps1

注意： 執行遊戲或提交測試前，請確認命令列開頭有顯示 (my-project-name)，代表虛擬環境已成功啟動。
3. 安裝 Pygame
將指定版本的 Pygame 加入專案相依套件中：

uv add pygame==2.6.1

4. 驗證安裝
確認 Pygame 是否已正確安裝至環境中：

uv run -m pygame

(執行後若看到 Pygame 的歡迎訊息與版本號，即代表安裝成功。)