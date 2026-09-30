# Environment Setup and Management

This guide explains how to set up your Python environment, install dependencies, and manage package requirements.

## 1. Create a Virtual Environment

It is recommended to use a virtual environment to manage dependencies.

**Windows (PowerShell):**
```powershell
python -m venv .venv
```

**macOS/Linux:**
```bash
python3 -m venv .venv
```

## 2. Activate the Environment

**Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate
```
*Note: If you see an execution policy error, run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`.*

**macOS/Linux:**
```bash
source .venv/bin/activate
```

## 3. Install Dependencies (Load)

To install all required packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

## 4. Save Environment (Save)

To save your current installed packages to `requirements.txt` (e.g., after installing a new package):

```bash
pip freeze > requirements.txt
```

## 5. Verify Installation

Check installed packages:
```bash
pip list
```

## 6. Alternative: Using uv (Fast Package Manager)

**Install uv:**
Windows (PowerShell):
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```
> [!IMPORTANT]
> After installing `uv`, you **MUST** restart your terminal (close and reopen it) for the `uv` command to be recognized.

macOS/Linux:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Usage:**
```bash
# Create virtual environment and install dependencies
uv sync

# Run Jupyter notebooks directly with uv
uv run jupyter lab
```
