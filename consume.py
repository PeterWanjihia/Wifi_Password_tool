# import requests

# url = 'http://localhost:8000/api/hello'

# try:
#     # Send GET request to the API
#     response = requests.get(url)

#     # Check if the request was successful (status code 200)
#     if response.status_code == 200:
#         # Parse and print the JSON response
#         data = response.json()
#         print(f"API Response: {data['message']}")
#     else:
#         print(f"Error: {response.status_code} - {response.text}")

# except Exception as e:
#     print(f"Error: {e}")
from http.server import HTTPServer, SimpleHTTPRequestHandler

# Set the host and port
host = "localhost"
port = 8000

# Create an HTTP server with the SimpleHTTPRequestHandler
server = HTTPServer((host, port), SimpleHTTPRequestHandler)

# Start the server
print(f"Server started on http://{host}:{port}")
server.serve_forever()
