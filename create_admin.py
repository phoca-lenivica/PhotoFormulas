from getpass import getpass
import sys
from PhotoFormulas import create_app
from PhotoFormulas.model import db, User

app = create_app()

with app.app_context():
	username = input('Введите имя пользователя:')

	if User.query.filter(User.username == username).count():
		print('Это имя уже занято!')
		sys.exit(0)

	password = getpass('Введите пароль')
	password2 = getpass('Повторите пароль')

	if not password == password2:
		print('Пароли не совпадают')
		sys.exit(0)

	new_user = User(username=username, role='admin')
	new_user.set_password(password)

	db.session.add(new_user)
	db.session.commit()
	print('Создан пользователь с id {}'.format(new_user.id))