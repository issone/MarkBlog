#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author:huchong
import os
from app import create_app, db
from app.models import User, Article
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app=app)
migrate = Migrate(app=app, db=db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Article=Article)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)
if __name__ == '__main__':
    manager.run()
