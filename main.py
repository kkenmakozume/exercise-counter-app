import counter_app
from counter_app import home_page, app, show, db


#root='/'
# increment ="increment"

database={'number': 0}

@app.route('/')
def home():
 # return show(home_page, number=database['number'])
  return 

@app.route('/increment')
def increment():
  database ['number']+=1
  print (database)
  return show(page=home_page, number=database['number'])

@app.route('/decrement')
def decrement():
  database ['number']-=1
  print (database)
  return show(page=home_page, number=database['number'])
app.run(host='0.0.0.0', port=81)
