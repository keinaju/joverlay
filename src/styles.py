from configuration import Configuration

def styles():
    return f"""
QTextEdit {{
    background-color: {Configuration.get("background-color", "rgba(0, 0, 0, 200)")};
    border: none;
    color: {Configuration.get("text-color", "rgba(255, 255, 255, 255)")};
    font-family: 'Consolas';
    font-size: 20px;
}}

QScrollBar:vertical {{
    background: rgba(255, 255, 255, 30);
    width: 8px;
}}

QScrollBar::handle:vertical {{
    background: rgba(255, 255, 255, 150);
    min-height: 20px;
}}
"""