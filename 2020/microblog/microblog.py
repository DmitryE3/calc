from app import app, db
from app.models import User, Post


# ф-я контекста оболочки, вызывется командой flask shell - регестрирует эл-ты в сеанс оболочки
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
