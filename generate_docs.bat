@echo off
python -m pip install --upgrade pip
pip install matplotlib numpy seaborn
python "docs\generate_images.py"