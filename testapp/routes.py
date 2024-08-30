"""クライアントからのリクエストに応じて、カメラから画像をキャプチャし、その画像を処理するエンドポイントを定義"""

from flask import current_app as app
from flask import jsonify, render_template, request

# from .openai_api import analyze_image
from .camera_get import start_main

# from . import create_app


print("Setting up app...")


def init_routes(app):
    @app.route("/")
    def index():
        print("Rendering index.html...")
        return render_template("index.html")

    @app.route("/capture", methods=["POST"])
    def capture():
        print("Capturing image...")
        try:
            image = start_main()
            return jsonify({"message": image})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return app
