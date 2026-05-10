import json
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
import os

def visualize():
    print("1. Loading processed data...")
    try:
        with open('processed_data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Error: processed_data.json not found. Please run Step 2 first.")
        return

    print("2. Loading HTML template...")
    
    file_loader = FileSystemLoader('.')
    env = Environment(loader=file_loader)
    
    try:
        template = env.get_template('template.html')
    except Exception as e:
        print(f"Error: template.html not found. {e}")
        return

    print("3. Rendering HTML...")
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    html_output = template.render(data=data, update_time=current_time)

    print("4. Saving index.html...")
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_output)
    
    print("Success! English report generated: index.html")

if __name__ == "__main__":
    visualize()