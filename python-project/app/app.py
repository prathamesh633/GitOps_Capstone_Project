import os
import yaml
from flask import Flask, render_template

app = Flask(__name__, template_folder="../templates")


def load_config():
    config_path = os.path.join(os.path.dirname(__file__), "../config/app_config.yaml")
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    return config


@app.route("/")
def index():
    config = load_config()
    return render_template("index.html", config=config)


@app.route("/health")
def health():
    return render_template("health.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # nosec B104