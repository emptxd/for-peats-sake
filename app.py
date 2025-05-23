from flask import Flask, render_template

app = Flask(__name__)

# === ROUTES ===

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/what-is-paludiculture')
def what_is_paludiculture():
    return render_template('what_is_paludiculture.html')

@app.route('/can-i-do-it')
def can_i_do_it():
    return render_template('can_i_do_it.html')


@app.route('/success-stories')
def success_stories():
    return render_template('success_stories.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')




# === MAIN ENTRY POINT ===
if __name__ == '__main__':
    app.run(debug=True)
