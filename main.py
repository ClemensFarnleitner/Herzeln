import webbrowser
import http.server
import socketserver
import os

# Set the path to your HTML file
html_file_path = '/Users/clemens/Herzeln/Herzeln/test.html'
text_file_path = '/Users/clemens/Herzeln/Herzeln/Test.txt'

# Read the content of the text file
with open(text_file_path, 'r') as file:
    file_content = file.read()

# Create a temporary directory for serving the modified HTML file
tmp_dir = 'tmp'
os.makedirs(tmp_dir, exist_ok=True)
os.chdir(tmp_dir)

# Read the HTML template file
with open(html_file_path, 'r') as file:
    html_template = file.read()

# Replace the placeholder in the HTML template with the file content
html_content = html_template.replace('{{fileContent}}', file_content)

# Save the modified HTML to a new file
with open('index.html', 'w') as file:
    file.write(html_content)

# Start a temporary server to serve the modified HTML file
PORT = 8001

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.getcwd(), **kwargs)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Server running at localhost:", PORT)
    webbrowser.open_new_tab(f'http://localhost:{PORT}/index.html')
    httpd.serve_forever()

