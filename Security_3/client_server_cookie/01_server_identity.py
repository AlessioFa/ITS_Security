from flask import Flask, request, redirect, make_response
from pathlib import Path

app = Flask(__name__)
STATIC_DIR = Path("static")

# ---------------------------
# Credenziali fisse
# ---------------------------
USER = "good_its_student"
PASS = "Andromeda77!_"

# ---------------------------
# Serve il form di login
# ---------------------------
@app.route("/")
def root():
    login_file = STATIC_DIR / "login.html"
    if not login_file.exists():
        return "<h1>404 - File non trovato</h1>", 404
    html = login_file.read_text(encoding="utf-8")
    resp = make_response(html, 200)
    resp.headers["Content-Type"] = "text/html; charset=utf-8"
    return resp

# ---------------------------
# Gestione login
# ---------------------------
@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == USER and password == PASS:
        # Credenziali corrette → imposta cookie e redirect alla pagina protetta
        resp = make_response(redirect("http://127.0.0.1:9000/protected"))
        resp.set_cookie("sessionid", "abc123", path="/")
        return resp
    else:
        # Credenziali sbagliate → redirect alla pagina di errore
        return redirect("http://127.0.0.1:9000/html/errore")

# ---------------------------
# Avvio server identity manager
# ---------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)

