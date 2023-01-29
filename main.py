from website import create_app

app = create_app()

#Only if we run this file are we going to execute the app
if __name__ == '__main__':
    app.run(debug = True, port=8000) #Runs the flask application (debug=True => Any change automatically reruns the web server)
