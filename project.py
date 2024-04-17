from flask import request, Flask, render_template, url_for, redirect, session, jsonify
from sqlalchemy import Column ,create_engine , String, ForeignKey, Date
from sqlalchemy.orm import DeclarativeBase , sessionmaker, Mapped, mapped_column

from flask_mail import Mail, Message

engine = create_engine("sqlite:///interesting_records.db", echo=True )

Session = sessionmaker(bind=engine)

app = Flask(__name__)
app.config['SECRET_KEY'] = '12212112'
#
app.config['MAIL_SERVER'] = 'smtp.ukr.net'
#
app.config['MAIL_PORT'] = 465
#
app.config['MAIL_USERNAME'] = 'sergggggggg@ukr.net'
#
app.config['MAIL_PASSWORD'] = '9VaSETJKppW7c5k6'
#
app.config['MAIL_DEFAULT_SENDER'] = 'sergggggggg@ukr.net'
#
app.config['MAIL_USE_TLS'] = False
#
app.config['MAIL_USE_SSL'] = True
#
mail = Mail(app)

keyboard_mapping = {
'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е',
'y': 'н', 'u': 'г', 'i': 'ш', 'o': 'щ', 'p': 'з',
'[': 'х', ']': 'ї', 'a': 'ф', 's': 'і', 'd': 'в',
'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л',
'l': 'д', ';': 'ж', "'": 'є', 'z': 'я', 'x': 'ч',
'c': 'с', 'v': 'м', 'b': 'и', 'n': 'т', 'm': 'ь',
',': 'б', '.': 'ю', '/': '.'
}

app.app_context().push()

# class Base(DeclarativeBase):
#     def create_db(self):
#         Base.metadata.create_all(engine)
#
#     def drop_db(self):
#         Base.metadata.drop_all(engine)
#
# class Users(Base):
#     __tablename__ = "users"
#     id : Mapped[int] = mapped_column(primary_key=True)
#     name : Mapped[str] = mapped_column(String(80))
#     password: Mapped[str] = mapped_column(String(140))
#     email: Mapped[str] = mapped_column(String(140))

@app.route('/')
def f():
    return render_template('main.html')

@app.route('/sign_up')
def f_1():
    return render_template('register.html')


@app.route('/login')
def f_2():
    return render_template('login.html')

@app.route('/translate')
def f__3():
    return render_template('translate.html')


@app.route('/signup', methods=['POST'])
def f_3():
    name = request.form['name']
    print(name)
    password = request.form['pass']
    user_email = request.form['email']
    # with Session() as session:
    #     new_user = Users(name=name, password=password,email=user_email)
    #     session.add(new_user)
    #     session.commit()
    #     session['user_id'] = new_user.id
    data = {'message': 'Ви зареєструвалися'}
    #     email_message = Message('Test', recipients=[user_email])
    #     email_message.body = 'text'
    #     mail.send(email_message)
    return jsonify(data),200


@app.route('/login',methods=['POST'])
def f_4():
    name = request.form['name']
    print(name)
    password = request.form['pass']
    # with Session() as session:
    #     user = session.query(Users).filter_by(name=name,password=password)
    #     if user:
    #         data = {'message': 'Ви увійшли в акаунт'}
    #         return jsonify(data)
    #     else:
    #         data = {'message': 'Ви ще не зареєстувалися'}
    #         return jsonify(data),200

@app.route('/translate',methods=['POST'])
def f_5():
    tr_text = request.form['tr_text']
    res = ''
    for i in tr_text:
        res += keyboard_mapping.get(i,'?')
    data = {'message': res }
    return jsonify(data),200

print(abs(-50+5))

if __name__ == '__main__':
    app.run(debug=True, port=8000)