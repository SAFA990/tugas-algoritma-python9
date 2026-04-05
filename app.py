from flask import Flask, render_template, request

app = Flask(__name__)

def hitung_biaya(harga, marketplace):
    if marketplace == "tokopedia":
        persen = 0.03
    elif marketplace == "shopee":
        persen = 0.04
    else:
        persen = 0.05

    biaya = harga * persen
    hasil = harga - biaya

    return biaya, hasil


@app.route('/', methods=['GET', 'POST'])
def index():
    biaya = None
    hasil = None

    if request.method == 'POST':
        harga = float(request.form['harga'])
        marketplace = request.form['marketplace']

        biaya, hasil = hitung_biaya(harga, marketplace)

    return render_template('index.html', biaya=biaya, hasil=hasil)


if __name__ == '__main__':
    app.run(debug=True)