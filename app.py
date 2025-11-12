from flask import Flask

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JL. Escobar Ponce Chevere</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #141E30, #243B55);
            color: #fff;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        h1 {
            font-size: 3rem;
            text-shadow: 0 0 20px rgba(255,255,255,0.2);
            margin-bottom: 0.5rem;
        }
        p {
            font-size: 1.2rem;
            opacity: 0.8;
        }
        a {
            margin-top: 1.5rem;
            display: inline-block;
            background: #00C9A7;
            color: #fff;
            padding: 0.8rem 1.6rem;
            border-radius: 30px;
            text-decoration: none;
            transition: 0.3s ease;
            font-weight: bold;
        }
        a:hover {
            background: #00E0BB;
            transform: translateY(-3px);
            box-shadow: 0 8px 15px rgba(0, 201, 167, 0.3);
        }
        footer {
            position: absolute;
            bottom: 15px;
            font-size: 0.9rem;
            opacity: 0.7;
        }
    </style>
</head>
<body>
    <h1>Bienvenido 🚀</h1>
    <p>Aplicación Flask diseñada por <strong>JL. Escobar Ponce</strong></p>
    <a href="/saludo/JL.escobarponce">Ver saludo personalizado</a>
    <footer>Powered by Flask & Traefik · 2025</footer>
</body>
</html>
"""

@app.route('/')
def home():
    return HTML_TEMPLATE

@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f"""
    <html>
        <head>
            <meta charset='UTF-8'>
            <title>Saludo de JL. Escobar Ponce</title>
            <style>
                body {{
                    background: radial-gradient(circle at top left, #243B55, #141E30);
                    color: #fff;
                    font-family: 'Segoe UI', sans-serif;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }}
                h2 {{
                    font-size: 2.5rem;
                    margin-bottom: 1rem;
                }}
                a {{
                    color: #00E0BB;
                    text-decoration: none;
                    font-weight: bold;
                    transition: 0.3s ease;
                }}
                a:hover {{
                    text-shadow: 0 0 10px #00E0BB;
                }}
            </style>
        </head>
        <body>
            <h2>Hola {nombre}, bienvenido a <strong>JL.escobarponce</strong> 🌟</h2>
            <a href="/">Volver al inicio</a>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
