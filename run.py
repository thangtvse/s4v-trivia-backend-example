from main import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("8080"), debug=True, threaded=True)
