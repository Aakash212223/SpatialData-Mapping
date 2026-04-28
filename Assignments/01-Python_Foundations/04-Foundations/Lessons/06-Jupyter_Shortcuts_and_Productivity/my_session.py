# coding: utf-8
- `A` → Insert cell Above
- `B` → Insert cell Below
- `D D` → Delete a cell
- `M` → Change to Markdown cell
- `Y` → Change to Code cell
- `Shift + Enter` → Run cell and move to next
- `Ctrl + Enter` → Run cell, stay put
- `Alt + Enter` → Run cell and insert new one below
get_ipython().run_line_magic('history', '-n 1-5  # Show the first 5 commands in this session')
# Save history to a file
get_ipython().run_line_magic('save', 'my_session.py 1-5')
