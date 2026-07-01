from flask import Flask, render_template_string

app = Flask(__name__)

pagina = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Para você ❤️</title>

<style>
body{
    background:#ffe6ec;
    display:flex;
    justify-content:center;
    align-items:center;
    height:100vh;
    font-family:Arial;
    text-align:center;
}

.caixa{
    background:white;
    padding:40px;
    border-radius:20px;
    box-shadow:0 0 20px rgba(0,0,0,.2);
    max-width:600px;
}

button{
    padding:15px 25px;
    font-size:18px;
    border:none;
    border-radius:12px;
    background:#ff4d88;
    color:white;
    cursor:pointer;
}
</style>

</head>

<body>

<div class="caixa">

<h1>Oii Minha Minion ❤️</h1>

<p>
Eu sei que errei com você e acabei mentindo por coisa besta.
</p>

<p>
Não fiz esse site para tentar apagar o que aconteceu.
Só queria assumir meu erro e pedir desculpas, E espero que isso não tenha criado uma barreira entre nós.
</p>

<p>
Você merece respeito e toda minha admiração 
e sinto muito por ter te machucado e mentido pra você.
</p>

<p>
Obrigado por dedicar alguns minutinhos seus para ler isso.
</p>

<button onclick="alert('Obrigado por me ouvir e Espero que me perdoe de Coração ❤️')">
Continuar
</button>

</div>

</body>
</html>
"""

@app.route("/")
def inicio():
    return render_template_string(pagina)

if __name__ == "__main__":
    app.run(debug=True)