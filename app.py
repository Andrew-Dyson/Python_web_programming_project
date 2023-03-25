from flask import Flask, render_template

from controllers.children_controller import children_blueprint


app = Flask(__name__)

app.register_blueprint(children_blueprint)


@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()