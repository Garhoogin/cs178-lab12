from flask import Flask, render_template

# Lab 12 - Declan Moore CS178
# Flask needs to know the name of this file to find templates and static files
app = Flask(__name__)

# ============================================================
#  ROUTE 1 — Home page
#  Visit: http://YOUR_IP:8080/
# ============================================================
@app.route('/')
def home():
    # render_template loads templates/home.html and sends it to the browser
    return render_template('home.html', page_title="My Flask Site")


# ============================================================
#  ROUTE 2 — Hello page with a URL variable
#  Visit: http://YOUR_IP:8080/hello/YourName/
#  Anything you put after /hello/ becomes the `name` variable
# ============================================================
@app.route('/hello/<name>/')
def hello(name):
    return render_template('hello.html', name=name)


def count_vowels(s):
    vowel_str = "aeiou"
    num_vowel = 0
    for c in s:
        if c in vowel_str:
            num_vowel += 1
    return num_vowel

# ============================================================
#  ROUTE 3 - Analze word with a URL variable
#  Visit: http://declan-ec2.garhoogin.com/analyze/Word
# ============================================================
@app.route('/analyze/<word>')
def analyze(word):
    # return "<pre>You entered:" + word + "<br/>Characters: " + str(len(word)) + \
    #     "<br/>Vowels: " + str(count_vowels(word)) + "<br/>Reversed: " + word[::-1] + "</pre>"
    return render_template('analyze.html', word=word, num_chars=len(word),
        num_vowels=count_vowels(word), word_rev=word[::-1])



# ============================================================
#  These two lines always stay at the bottom of the file.
#  host='0.0.0.0' means "listen on all network interfaces"
#  so the server is reachable from outside EC2, not just locally
# ============================================================
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
