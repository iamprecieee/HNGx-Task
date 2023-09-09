# from task import create_app

# if __name__ == "__main__":
#     app = create_app()
#     app.run()


from resources import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)