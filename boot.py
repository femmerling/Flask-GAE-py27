from google.appengine.ext.appstats import recording
import sys, os

root_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(root_dir, 'libs'))

from main import app

if 'SERVER_SOFTWARE' in os.environ and os.environ['SERVER_SOFTWARE'].startswith('Dev'):
    import debug.utils
    sys.modules['werkzeug.debug.utils'] = debug.utils

    import inspect
    inspect.getsourcefile = inspect.getfile

    from werkzeug import DebuggedApplication
    app = DebuggedApplication(app, evalex=True)

app = recording.appstats_wsgi_middleware(app)

