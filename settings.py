SECRET_KEY = '2343SDEWQERsHwer&^23cA'
# Set the database connection string
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Vff123456@127.0.0.1/yuhu?charset=UTF8MB4'
# Do not track changes, do not set there will be warnings
SQLALCHEMY_TRACK_MODIFICATIONS = False
JSON_AS_ASCII = False

# JWT设置
# JWT access token expiration time (second)
JWT_ACCESS_TOKEN_EXPIRES = 60