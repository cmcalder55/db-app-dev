import dash
from dashboard import layouts

app = dash.Dash(__name__)
app.title = 'Senior Design Program'
app.layout = layouts.init(app)
