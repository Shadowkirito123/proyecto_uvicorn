from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3]

@app.get('/contacto', response_class= HTMLResponse)
def get_list():
    return """
        <style>
            body{
                color: red;
            }
        </style>
        <h1 class='texto'>Hola soy una pagina web</h1>
        <p>Parrafo</p>

    """