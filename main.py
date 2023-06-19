import webbrowser
import http.server
import socketserver
import os

# Set the path to your HTML file
html_file_path = '/Users/clemens/Herzeln/Herzeln/test.html'

# Create a temporary directory for serving the HTML file
tmp_dir = 'tmp'
os.makedirs(tmp_dir, exist_ok=True)
os.chdir(tmp_dir)
with open(html_file_path, 'r') as file:
    html_content = file.read()
with open('index.html', 'w') as file:
    file.write(html_content)

# Start a temporary server to serve the HTML file
PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.getcwd(), **kwargs)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Server running at localhost:", PORT)
    webbrowser.open_new_tab(f'http://localhost:{PORT}/index.html')
    httpd.serve_forever()
