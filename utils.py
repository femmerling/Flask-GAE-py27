import uuid
from datetime import datetime
import re

_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')

def generate_id():
    return str(uuid.uuid4())

def datetime_to_unix(timestamp):
    epoch = datetime.utcfromtimestamp(0)
    return long((timestamp-epoch).total_seconds())

def unix_to_datetime(unixtime):
    return datetime.utcfromtimestamp(long(unixtime))

def generate_slug(text, delim=u'-'):
    extra=datetime_to_unix(datetime.now())
    result = []
    for word in _punct_re.split(text.lower()):
        result.extend(word.split())
    result = delim.join(result)
    return '%s-%s' % (extra, result)
