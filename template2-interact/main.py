
from datetime import datetime

import dash_mantine_components as dmc
from dash import Dash, dcc, html, _dash_renderer, Input, Output, State,callback
from dash_mantine_components import MantineProvider

# Veja se essa config não foi atualizada
_dash_renderer._set_react_version('18.2.0')

app = Dash(name="template1-static", title="nome", external_stylesheets=[dmc.styles.ALL])




app.layout = dmc.MantineProvider([])
if __name__ == '__main__': app.run_server(debug=True)