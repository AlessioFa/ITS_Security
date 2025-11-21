from flask import Flask, make_response, redirect, request
from pathlib import Path

# create the flask application instance
app = Flask(__name__)

# define the directory where static HTML files are stored
STATIC_DIR = Path("static")


def serve_html(filename: str):

    # Construct the full path to the requested file
    path = STATIC_DIR / filename

    # Check if the file exists
    if not path.exists():
        # Return a 404 Not Found response if the file is missing
        return make_response("<h1>404 - File not found</h1>", 404)

    # Read the content of the HTML file
    html = path.read_text(encoding="utf-8")

    # Create the response object with the HTML content and a 200 OK status
    resp = make_response(html, 200)

    # Explicitly set the content type header for HTML
    resp.headers["Content-Type"] = "text/html; charset=utf-8"
    return resp


@app.route("/html/<page>")
def html_page(page):
    """
    Renders an HTML page dynamically based on the URL path.
    Example: /html/home will look for static/home.html.
    """
    # The page variable is used to construct the full filename
    return serve_html(f"{page}.html")


@app.route("/")
def root():
    """
    Shortcut route to serve the default homepage.
    """
    # Serves the home.html file
    return serve_html("home.html")


@app.route("/go/<target>")
def go(target):
    """
    Performs an HTTP 302 (Found/Temporary Redirect) to another internal path.
    Example: /go/error redirects the browser to /html/error.
    """
    # Returns a redirect response to the specified target page
    return redirect(f"/html/{target}", code=302)


@app.route("/setcookie")
def setcookie():
    """
    Sets a simple sessionid cookie in the client's browser and then
    serves the home page. This simulates the Identity Manager setting
    a successful authentication cookie.
    """
    # Get the HTML response for the home page first
    resp = serve_html("home.html")

    # Set the 'sessionid' cookie with a simple value
    # path="/" ensures the cookie is sent with requests to any path on this domain
    resp.set_cookie("sessionid", "abc123", path="/")
    return resp


@app.route("/showcookie")
def showcookie():
    """
    Displays all cookies received from the client in the request headers.
    This helps visualize what data the client is sending to the server.
    """
    # request.cookies is a dictionary of all cookies sent by the client
    cookies = request.cookies

    # Prepare the HTML response body
    html = "<h1>Received Cookies</h1><pre>"
    for k, v in cookies.items():
        html += f"{k} = {v}\n"
    html += "</pre><a href='/'>Back to home</a>"

    # Create and return the final response
    resp = make_response(html, 200)
    resp.headers["Content-Type"] = "text/html; charset=utf-8"
    return resp


@app.route("/protected")
def protected():
    """
    A protected resource that requires a specific cookie to be present
    for access. This simulates an authorization check.
    """
    # Check if the 'sessionid' cookie is present and has the expected value
    if request.cookies.get("sessionid") != "abc123":
        # If the required cookie is missing or incorrect, redirect to an error page
        # This is a basic form of authorization failure
        return redirect("/html/errore", code=302)

    # If the check passes, serve the protected content
    return serve_html("protected.html")


# Server initialization block
if __name__ == "__main__":
    # Ensure the static directory exists before starting the server
    STATIC_DIR.mkdir(exist_ok=True)
    # Start the Flask development server on all interfaces (0.0.0.0)
    # and port 9000. Debug mode enables automatic reloading.
    app.run(host="0.0.0.0", port=9000, debug=True)
