# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from datetime import datetime
from flask import Flask, redirect, render_template, request
from google.cloud import datastore

try:
    from urllib import urlencode
except Exception:
    from urllib.parse import urlencode

app = Flask(__name__)
client = datastore.Client()


@app.route('/', methods=['GET'])
def display_guestbook():
    guestbook_name = request.args.get('guestbook_name', '')
    print('GET guestbook name is {}'.format(guestbook_name))
    ancestor_key = client.key('Book', guestbook_name or "*notitle*")
    greetings = client.query(ancestor=ancestor_key).fetch(limit=20)

    greeting_blockquotes = [greeting.get('content', '') for greeting in greetings]
    return render_template(
            'index.html',
            greeting_blockquotes=greeting_blockquotes,
            guestbook_name=guestbook_name
        )


@app.route('/sign', methods=['POST'])
def update_guestbook():
    # We set the parent key on each 'Greeting' to ensure each guestbook's
    # greetings are in the same entity group.
    guestbook_name = request.form.get('guestbook_name', '')
    print('Guestbook name from the form: {}'.format(guestbook_name))

    print('Guestbook name from the URL: {}'.format(guestbook_name))
    ancestor_key = client.key('Book', guestbook_name or "*notitle*")
    key = client.key('Greeting', parent=ancestor_key)
    greeting = datastore.Entity(key=key)
    greeting['content'] = request.form.get('content', None)
    greeting['date'] = datetime.utcnow()
    client.put(greeting)

    return redirect('/?' + urlencode({'guestbook_name': guestbook_name}))


if __name__ == '__main__':
    # This is used when running locally.
    app.run(host='127.0.0.1', port=8080, debug=True)
