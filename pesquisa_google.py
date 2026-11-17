import webbrowser
from urllib.parse import quote_plus

termo = "roberty"
url = f"https://www.google.com/search?q={quote_plus(termo)}"

webbrowser.open(url)
