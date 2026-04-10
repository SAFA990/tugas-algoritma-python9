from flask import Flask, render_template, request

app = Flask(__name__)

# Fungsi untuk menghitung engagement rate
def hitung_engagement(like, comment, share, followers):
    return (like + comment + share) / followers * 100


@app.route('/', methods=['GET', 'POST'])
def index():
    hasil = None
    keterangan = ""
    error = ""

    if request.method == 'POST':
        try:
            like = int(request.form['like'])
            comment = int(request.form['comment'])
            share = int(request.form['share'])
            followers = int(request.form['followers'])

            # Validasi input
            if like < 0 or comment < 0 or share < 0 or followers <= 0:
                error = "Input tidak boleh negatif dan followers tidak boleh nol!"
            else:
                hasil = hitung_engagement(like, comment, share, followers)

                # Keterangan hasil
                if hasil < 1:
                    keterangan = "Engagement Rendah"
                elif 1 <= hasil <= 5:
                    keterangan = "Engagement Sedang"
                else:
                    keterangan = "Engagement Tinggi"

        except:
            error = "Semua input harus diisi dengan angka!"

    return render_template('index.html', hasil=hasil, keterangan=keterangan, error=error)


if __name__ == '__main__':
    app.run(debug=True)