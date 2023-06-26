from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) # This means that it will rerun every time we make changes to our code.
