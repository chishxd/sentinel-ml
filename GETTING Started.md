# 📚 Sentinel-ML — Setup Guide (Windows)

Hey teammate! Follow this exactly — no shortcuts.

---

## ✅ 1️⃣ Install Python

- Download [Python 3.11+](https://www.python.org/downloads/windows/)
- During setup, ✅ **tick “Add Python to PATH”**

---

## ✅ 2️⃣ Install Git

- Download [Git for Windows](https://git-scm.com/download/win)
- During setup:
  - ✅ “Checkout as-is, commit Unix-style line endings”
  - ✅ “Use Git from the command line and also from 3rd-party software”
  - ✅ Use **OpenSSH** (default)

---

## ✅ 3️⃣ Set up your SSH key (once)

1. Open Git Bash:
   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com"
   ```
Just press enter 3 times.

2. Show your public key:

   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```

3. Copy that key and add it to your GitHub:

   * [Add SSH key to GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)

---

## ✅ 4️⃣ Install Poetry

Open **PowerShell** (not CMD):

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

Verify:

```powershell
poetry --version
```

---

## ✅ 5️⃣ Clone the project

```powershell
cd path\to\your\projects
git clone git@github.com:chishxd/sentinel-ml.git
cd sentinel-ml
```

---

## ✅ 6️⃣ Always keep your `.venv` inside the project

```powershell
poetry config virtualenvs.in-project true
```

---

## ✅ 7️⃣ Install dependencies

```powershell
poetry install
```

---

## ✅ 8️⃣ Activate your virtual environment

```powershell
poetry shell
```

Your prompt should look like:

```
(.venv) PS C:\path\to\sentinel-ml>
```

---

## ✅ 9️⃣ Run the project

```powershell
python -m sentinel_ml.main
```

---

## ✅ 1️⃣0️⃣ VSCode tips

* Open the **project folder** in VSCode.
* `Python: Select Interpreter` → pick the one in `.venv`.
* VSCode terminal should auto-run:

  ```
  source .venv/Scripts/activate
  ```
* Run and debug normally.

---

## ⚡ Common commands

| What?            | Command                          |
| ---------------- | -------------------------------- |
| Update code      | `git pull origin dev`            |
| Install deps     | `poetry install`                 |
| Run scripts      | `poetry shell` → `python -m ...` |
| Add a package    | `poetry add package_name`        |
| Remove a package | `poetry remove package_name`     |
| Run tests        | `poetry run pytest`              |

---

## 💡 Troubleshooting

✅ Use **PowerShell** or **Git Bash**, not old CMD.
✅ If SSH push gives `permission denied`, re-check your SSH key.
✅ If VSCode runs the wrong Python, re-select the `.venv` interpreter.

---

You’re good to go! 🚀
