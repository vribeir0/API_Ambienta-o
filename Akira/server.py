<<<<<<< HEAD
from flask import Flask, url_for, render_template, request, jsonify
from flask_ldap3_login import LDAP3LoginManager
from flask_login import LoginManager, login_user, UserMixin, current_user, login_required, logout_user
from flask import render_template_string, redirect
from flask_ldap3_login.forms import LDAPLoginForm
from db import *
import time
import spacy


app = Flask(__name__,template_folder='templates',static_url_path='/static')
app.config['SECRET_KEY'] = '########'
#remover o debug True quando projeto estiver entregue e rodando
app.config['DEBUG'] = True

# Setup LDAP Configuration Variables.
# Hostname of your LDAP Server
app.config['LDAP_HOST'] = '######'
# Base DN of your directory
app.config['LDAP_BASE_DN'] = '######'
# Users DN to be prepended to the Base DN
app.config['LDAP_USER_DN'] = '######'
# The RDN attribute for your user schema on LDAP
app.config['LDAP_USER_RDN_ATTR'] = '#######'
# The Attribute you want users to authenticate to LDAP with.
app.config['LDAP_USER_LOGIN_ATTR'] = '#####'
# The Username to bind to LDAP with
app.config['LDAP_BIND_USER_DN'] = None
# The Password to bind to LDAP with
app.config['LDAP_BIND_USER_PASSWORD'] = None

login_manager = LoginManager(app)              # Setup a Flask-Login Manager
ldap_manager = LDAP3LoginManager(app)          # Setup a LDAP3 Login Manager.

# Create a dictionary to store the users in when they authenticate, memory
users = {}

#pagina inexistente (correção)
@app.errorhandler(404)
def not_found(e):
    # return ('pagina de erro mpf')
    if current_user.is_authenticated:
        return render_template('erro.html')
    else:
        return redirect(url_for('login'))

# Declare an Object Model for the user, and make it comply with the
# flask-login UserMixin mixin.
class User(UserMixin):
    def __init__(self, dn, username, data):
        self.dn = dn
        self.username = username
        self.data = data

    def __repr__(self):
        return self.dn

    def get_id(self):
        return self.dn
def remove_keyvalue():
    del users[str(current_user)]

# Declare a User Loader for Flask-Login.
# Simply returns the User if it exists in our 'database', otherwise
# returns None.
@login_manager.user_loader
def load_user(id):
    if id in users:
        return users[id]
    return None


# Declare The User Saver for Flask-Ldap3-Login
# This method is called whenever a LDAPLoginForm() successfully validates.
# Here you have to save the user, and return it so it can be used in the
# login controller.
@ldap_manager.save_user
def save_user(dn, username, data, memberships):
    user = User(dn, username, data)
    users[dn] = user
    return user

# Declaração de rotas
@app.route('/')
def home():
    # Redirect users who are not logged in.
    # if not current_user or current_user.is_anonymous:
    #     return redirect(url_for('login'))
    # User is logged in, so show them a page with their cn and dn.
    db = DataBase()
    conteudo = db.getConteudo()
    print('Conteudo :' + str(conteudo) + '\n')
    categoria = db.getCategoria()
    # print('Categoria :' + str(categoria) + '\n')
    subCategoria = db.getSubCategoria()
    # print('Subcategoria :' + str(subCategoria) + '\n')
    return render_template('index.html',conteudos = conteudo, categorias = categoria, subCategorias = subCategoria)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Instantiate a LDAPLoginForm which has a validator to check if the user
    # exists in LDAP.
    form = LDAPLoginForm()
    consultaBot()
    if request.method=="POST":
        if form.validate_on_submit():
            # Successfully logged in, We can now access the saved user object
            # via form.user.
            login_user(form.user)  # Tell flask-login to log them in.
            return redirect('/')  # Send them home
        else:
            #erro de login aqui
            return render_template('login.html', form=form, var=1)
    if request.method=="GET":
        return render_template('login.html',form=form, var=0)
    
#Inicio dos testes de processamento de linguagem natural
def consultaBot():
    nlp = spacy.load('pt_core_news_md')
    fraseUsuario = nlp('Meu teclado está apresentando inconsistencias nas teclas apertadas, quando eu aperto uma tecla aparece outra diferente')    

    for aux in fraseUsuario:
        print(aux.orth_ + ' -> ' + aux.pos_)
    
@app.route('/logout')
def logout():
    if current_user.is_authenticated:
        remove_keyvalue()
        logout_user()
        return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

@app.route('/admin')
def admin():
    if current_user.is_authenticated:
        return render_template('admin/admin.html')
    else:
        return redirect(url_for('logout'))

@app.route('/admin_cd')
def admin_cd():
    if current_user.is_authenticated:
        return render_template('admin/admin_cd.html')
    else:
        return redirect(url_for('logout'))

@app.route('/admin_ca')
def admin_ca():
    if current_user.is_authenticated:
        return render_template('admin/admin_ca.html')
    else:
        return redirect(url_for('logout'))

@app.route('/admin_up')
def admin_up():
    if current_user.is_authenticated:
        return render_template('admin/admin_up.html')
    else:
        return redirect(url_for('logout'))

@app.route('/admin_del')
def admin_del():
    if current_user.is_authenticated:
        return render_template('admin/admin_del.html')
    else:
        return redirect(url_for('logout'))


if __name__ == '__main__':
=======
from flask import Flask, url_for, render_template, request, jsonify
from flask_ldap3_login import LDAP3LoginManager
from flask_login import LoginManager, login_user, UserMixin, current_user, login_required, logout_user
from flask import render_template_string, redirect
from flask_ldap3_login.forms import LDAPLoginForm
from db import *
import time
import spacy


app = Flask(__name__,template_folder='templates',static_url_path='/static')
app.config['SECRET_KEY'] = '########'
#remover o debug True quando projeto estiver entregue e rodando
app.config['DEBUG'] = True

# Setup LDAP Configuration Variables.
# Hostname of your LDAP Server
app.config['LDAP_HOST'] = '######'
# Base DN of your directory
app.config['LDAP_BASE_DN'] = '######'
# Users DN to be prepended to the Base DN
app.config['LDAP_USER_DN'] = '######'
# The RDN attribute for your user schema on LDAP
app.config['LDAP_USER_RDN_ATTR'] = '#######'
# The Attribute you want users to authenticate to LDAP with.
app.config['LDAP_USER_LOGIN_ATTR'] = '#####'
# The Username to bind to LDAP with
app.config['LDAP_BIND_USER_DN'] = None
# The Password to bind to LDAP with
app.config['LDAP_BIND_USER_PASSWORD'] = None

login_manager = LoginManager(app)              # Setup a Flask-Login Manager
ldap_manager = LDAP3LoginManager(app)          # Setup a LDAP3 Login Manager.

# Create a dictionary to store the users in when they authenticate, memory
users = {}

#pagina inexistente (correção)
@app.errorhandler(404)
def not_found(e):
    # return ('pagina de erro mpf')
    if current_user.is_authenticated:
        return render_template('erro.html')
    else:
        return redirect(url_for('login'))

# Declare an Object Model for the user, and make it comply with the
# flask-login UserMixin mixin.
class User(UserMixin):
    def __init__(self, dn, username, data):
        self.dn = dn
        self.username = username
        self.data = data

    def __repr__(self):
        return self.dn

    def get_id(self):
        return self.dn
def remove_keyvalue():
    del users[str(current_user)]

# Declare a User Loader for Flask-Login.
# Simply returns the User if it exists in our 'database', otherwise
# returns None.
@login_manager.user_loader
def load_user(id):
    if id in users:
        return users[id]
    return None


# Declare The User Saver for Flask-Ldap3-Login
# This method is called whenever a LDAPLoginForm() successfully validates.
# Here you have to save the user, and return it so it can be used in the
# login controller.
@ldap_manager.save_user
def save_user(dn, username, data, memberships):
    user = User(dn, username, data)
    users[dn] = user
    return user

# Declaração de rotas
@app.route('/')
def home():
    # Redirect users who are not logged in.
    # if not current_user or current_user.is_anonymous:
    #     return redirect(url_for('login'))
    # User is logged in, so show them a page with their cn and dn.
    db = DataBase()
    conteudo = db.getConteudo()
    print('Conteudo :' + str(conteudo) + '\n')
    categoria = db.getCategoria()
    # print('Categoria :' + str(categoria) + '\n')
    subCategoria = db.getSubCategoria()
    # print('Subcategoria :' + str(subCategoria) + '\n')
    return render_template('index.html',conteudos = conteudo, categorias = categoria, subCategorias = subCategoria)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Instantiate a LDAPLoginForm which has a validator to check if the user
    # exists in LDAP.
    form = LDAPLoginForm()
    consultaBot()
    if request.method=="POST":
        if form.validate_on_submit():
            # Successfully logged in, We can now access the saved user object
            # via form.user.
            login_user(form.user)  # Tell flask-login to log them in.
            return redirect('/')  # Send them home
        else:
            #erro de login aqui
            return render_template('login.html', form=form, var=1)
    if request.method=="GET":
        return render_template('login.html',form=form, var=0)
    
#Inicio dos testes de processamento de linguagem natural
def consultaBot():
    nlp = spacy.load('pt_core_news_md')
    fraseUsuario = nlp('Meu teclado está apresentando inconsistencias nas teclas apertadas, quando eu aperto uma tecla aparece outra diferente')    

    for aux in fraseUsuario:
        print(aux.orth_ + ' -> ' + aux.pos_)
    
@app.route('/logout')
def logout():
    if current_user.is_authenticated:
        remove_keyvalue()
        logout_user()
        return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

@app.route('/admin')
def admin():
    if current_user.is_authenticated:
        return render_template('admin/admin.html')
    else:
        return redirect(url_for('logout'))

@app.route('/admin_cd')
def admin_cd():
    if current_user.is_authenticated:
        return render_template('admin/admin_cd.html')
    else:
        return redirect(url_for('logout'))

@app.route('/admin_ca')
def admin_ca():
    if current_user.is_authenticated:
        return render_template('admin/admin_ca.html')
    else:
        return redirect(url_for('logout'))

@app.route('/admin_up')
def admin_up():
    if current_user.is_authenticated:
        return render_template('admin/admin_up.html')
    else:
        return redirect(url_for('logout'))

@app.route('/admin_del')
def admin_del():
    if current_user.is_authenticated:
        return render_template('admin/admin_del.html')
    else:
        return redirect(url_for('logout'))


if __name__ == '__main__':
>>>>>>> 0d4cd1d948740476286dfb12d91439f8529fd3c1
    app.run()