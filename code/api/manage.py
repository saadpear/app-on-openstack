from flask.ext.script import Manager

from watermark.models import db, Image
from watermark.app import create_app

app = create_app()
manager = Manager(app)


@manager.command
def create_all():
    db.create_all()
    dummy_data()

@manager.command
def drop_all():
    db.drop_all()

@manager.command
def dummy_data():
    test_image_1 = Image(href="https://github.com/danabauer/app-on-openstack/blob/gh-pages/presentation/img/shasta-lake-web.jpg")
    db.session.add_all([test_image_1])
    db.session.commit()


if __name__ == '__main__':
    manager.run()
