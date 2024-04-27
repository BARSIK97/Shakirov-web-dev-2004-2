from flask import Flask, render_template, session, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from mysqldb import DBConnector
from mysql.connector.errors import DatabaseError


app = Flask(__name__)
application = app
app.config.from_pyfile('config.py')

db_connector = DBConnector(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth"
login_manager.login_message = "Войдите, чтобы просматривать содержимое данной страницы"
login_manager.login_message_category = "warning"

class User(UserMixin):
    def __init__(self, user_id, login):
        self.id = user_id
        self.login = login


CREATE_USER_FIELDS = ['login', 'password', 'last_name', 'first_name', 'middle_name', 'role_id']
EDIT_USER_FIELDS = ['last_name', 'first_name', 'middle_name', 'role_id']

def get_roles():
    query = "SELECT * FROM roles"

    with db_connector.connect().cursor(named_tuple=True) as cursor:
        cursor.execute(query)
        roles = cursor.fetchall()
    return roles


@login_manager.user_loader
def load_user(user_id):
    query = "SELECT id, login FROM users WHERE id=%s"

    with db_connector.connect().cursor(named_tuple=True) as cursor:

        cursor.execute(query, (user_id,))
        user = cursor.fetchone()

    if user:
        return User(user_id, user.login)
    
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/auth', methods=["GET", "POST"])
def auth():
    if request.method == "GET":
        return render_template("auth.html")
    
    login = request.form.get("login", "")
    password = request.form.get("pass", "")
    remember = request.form.get("remember") == "on"

    query = 'SELECT id, login FROM users WHERE login=%s AND password=SHA2(%s, 256)'
    
    print(query)

    with db_connector.connect().cursor(named_tuple=True) as cursor:

        cursor.execute(query, (login, password))

        print(cursor.statement)

        user = cursor.fetchone()

    if user:
        login_user(User(user.id, user.login), remember=remember)
        flash("Вы успешно вошли", category="success")
        target_page = request.args.get("next", url_for("index"))
        return redirect(target_page)

    flash("Введен неверный логин или пароль", category="danger")    

    return render_template("auth.html")

@app.route('/users')
def users():
    query = 'SELECT users.*, roles.name as role_name FROM users LEFT JOIN roles ON users.role_id = roles.id'

    with db_connector.connect().cursor(named_tuple=True) as cursor:
        cursor.execute(query)
        data = cursor.fetchall() 

    return render_template("users.html", users=data)

def get_form_data(required_fields):
    user = {}

    for field in required_fields:
        user[field] = request.form.get(field) or None

    return user

@app.route('/users/<int:user_id>/view')
def view_user(user_id):
    query = 'SELECT users.*, roles.name as role_name FROM users LEFT JOIN roles ON users.role_id = roles.id WHERE users.id = %s'
    with db_connector.connect().cursor(named_tuple=True) as cursor:
        cursor.execute(query, (user_id,))
        user = cursor.fetchone()

    return render_template("view_user.html", user=user)

@app.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    query = ("SELECT * FROM users where id = %s")
    roles = get_roles()
    with db_connector.connect().cursor(named_tuple=True) as cursor:
        cursor.execute(query, (user_id, ))
        user = cursor.fetchone()

    if request.method == "POST":
        user = get_form_data(EDIT_USER_FIELDS)
        user['user_id'] = user_id
        query = ("UPDATE users "
                 "SET last_name=%(last_name)s, first_name=%(first_name)s, "
                 "middle_name=%(middle_name)s, role_id=%(role_id)s "
                 "WHERE id=%(user_id)s ")

        try:
            with db_connector.connect().cursor(named_tuple=True) as cursor:
                cursor.execute(query, user)
                db_connector.connect().commit()
            
            flash("Вы успешно обновили пользователя", category="success")
            return redirect(url_for('users'))
        except DatabaseError as error:
            flash(f'Ошибка при обновление пользователя {error}', category="danger")
            db_connector.connect().rollback()    

    return render_template("edit_user.html", user=user, roles=roles)

@app.route('/users/<int:user_id>/delete', methods=["POST"])
@login_required
def delete_user(user_id):
    query = "DELETE FROM users WHERE id=%s"

    try:
        with db_connector.connect().cursor(named_tuple=True) as cursor:
            cursor.execute(query, (user_id, ))
            db_connector.connect().commit() 
        
        flash("Вы успешно удалили пользователя", category="success")
    except DatabaseError as error:
        flash(f'Ошибка удаления пользователя {error}', category="danger")
        db_connector.connect().rollback()    
    
    return redirect(url_for('users'))

@app.route('/users/new', methods=['GET', 'POST'])
@login_required
def create_user():
    user = {}
    roles = get_roles()
    errors = None
    query = ("INSERT INTO users "
             "(login, password, last_name, first_name, middle_name, role_id, creation_date) "
             "VALUES (%(login)s, SHA2(%(password)s, 256), "
             "%(last_name)s, %(first_name)s, %(middle_name)s, %(role_id)s, CURRENT_DATE)")
    if request.method == 'POST':
        user = get_form_data(CREATE_USER_FIELDS)
        
        errors = validate_user_data(user)
        
        if not errors:
            try:
                with db_connector.connect().cursor(named_tuple=True) as cursor:
                    cursor.execute(query, user)
                    db_connector.connect().commit()
                    flash("Вы успешно создали пользователя", category="success")
                return redirect(url_for('users'))
            except DatabaseError as error:
                flash(f'Ошибка создания пользователя {error}', category="danger")    
                db_connector.connect().rollback()
 
    return render_template("user_form.html", user=user, roles=roles, errors=errors)

def validate_user_data(user):
    errors = {}

    if not user['login'] or len(user['login']) <= 5 or not user['login'].isalnum():
        errors['login'] = 'Логин должен содержать не менее 5 символов и состоять только из латинских букв и цифр'

    if not user['password'] or len(user['password']) <= 8 or len(user['password']) > 128:
        errors['password'] = 'Пароль должен содержать от 8 до 128 символов'
    elif not any(char.isupper() for char in user['password']):
        errors['password'] = 'Пароль должен содержать хотя бы одну заглавную букву'
    elif not any(char.islower() for char in user['password']):
        errors['password'] = 'Пароль должен содержать хотя бы одну строчную букву'
    elif not any(char.isdigit() for char in user['password']):
        errors['password'] = 'Пароль должен содержать хотя бы одну цифру'
    elif not all(char.isalnum() or char in '~!@#$%^&*_-+()[]{}><\/|"\'.,:;' for char in user['password']):
        errors['password'] = 'Пароль должен содержать только латинские или кириллические буквы, арабские цифры и допустимые символы (~!@#$%^&*_-+()[]{}><\/|"\'.,:;)'

    if not user['last_name']:
        errors['last_name'] = 'Поле не может быть пустым'
    if not user['first_name']:
        errors['first_name'] = 'Поле не может быть пустым'

    return errors

@app.route('/change_pass', methods=['GET', 'POST'])
@login_required
def change_pass():
    if request.method == 'POST':
        old_password = request.form.get('old_password', '')
        new_password = request.form.get('new_password', '')
        confirm_password = request.form.get('confirm_password', '')

        user = current_user
        query = 'SELECT password FROM users WHERE id=%s AND password=SHA2(%s, 256)'
        with db_connector.connect().cursor() as cursor:
            cursor.execute(query, (user.id, old_password))
            result = cursor.fetchone()
        
        if not result:
            flash('Введен неверный текущий пароль', category='danger')
            return redirect(url_for('change_pass'))

        if new_password != confirm_password:
            flash('Новый пароль и его подтверждение не совпадают', category='danger')
            return redirect(url_for('change_pass'))
        
        errors = validate_password(new_password)
        if errors:
            flash('Новый пароль не соответствует требованиям: {}'.format(', '.join(errors.values())), category='danger')
            return redirect(url_for('change_pass'))

        update_query = 'UPDATE users SET password=SHA2(%s, 256) WHERE id=%s'
        try:
            with db_connector.connect().cursor() as update_cursor:
                update_cursor.execute(update_query, (new_password, user.id))
                db_connector.connect().commit()
            flash('Пароль успешно изменен', category='success')
        except DatabaseError as error:
            flash(f'Ошибка при изменении пароля: {error}', category='danger')
            db_connector.connect().rollback()

    return render_template('change_pass.html')

def validate_password(password):
    errors = {}

    if len(password) <= 8 or len(password) > 128:
        errors['password'] = 'Пароль должен содержать от 8 до 128 символов'
    elif not any(char.isupper() for char in password):
        errors['password'] = 'Пароль должен содержать хотя бы одну заглавную букву'
    elif not any(char.islower() for char in password):
        errors['password'] = 'Пароль должен содержать хотя бы одну строчную букву'
    elif not any(char.isdigit() for char in password):
        errors['password'] = 'Пароль должен содержать хотя бы одну цифру'
    elif not all(char.isalnum() or char in '~!@#$%^&*_-+()[]{}><\/|"\'.,:;' for char in password):
        errors['password'] = 'Пароль должен содержать только латинские или кириллические буквы, арабские цифры и допустимые символы (~!@#$%^&*_-+()[]{}><\/|"\'.,:;)'

    return errors



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route('/secret')
@login_required
def secret():
    return render_template('secret.html')