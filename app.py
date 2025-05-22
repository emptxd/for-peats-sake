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

@app.route('/biomass-uses')
def biomass_uses():
    return render_template('biomass_uses.html')

@app.route('/success-stories')
def success_stories():
    return render_template('success_stories.html')

@app.route('/policymakers')
def policymakers():
    return render_template('policymakers.html')

@app.route('/learn-more')
def learn_more():
    return render_template('learn_more.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/downloads')
def downloads():
    return render_template('downloads.html')


# === MAIN ENTRY POINT ===
if __name__ == '__main__':
    app.run(debug=True)
