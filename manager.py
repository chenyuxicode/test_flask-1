from application import create_app, db

def main():
    app = create_app('settings')
    app.run('0.0.0.0', debug=True, port=5000, ssl_context=('fullchain.pem', 'privkey.pem'))

if __name__ == '__main__':
    main()