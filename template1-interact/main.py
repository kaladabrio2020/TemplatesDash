
from datetime import datetime

import dash_mantine_components as dmc
from dash import Dash, dcc, html, _dash_renderer, Input, Output, State,callback
from dash_mantine_components import MantineProvider

# Veja se essa config não foi atualizada
_dash_renderer._set_react_version('18.2.0')

app = Dash(name="template1-static", title="nome", external_stylesheets=[dmc.styles.ALL])

# Outras configs importantes
configs = {'displaylogo': False, 'displayModeBar':False} # remove o logo do dash

# COLOQUE OS GRAFICOS ABAIXO

## exemplo 
import plotly.graph_objects as go
fig = go.Figure()
fig.update_layout(height=300)


## --------------------------

## Linha 0 - Coloque os cards
configsCard        = dict(withBorder=True, shadow="sm", radius="md")
configsCardSection = dict(withBorder=True, inheritPadding=True, py="xs")

linha0 = dmc.Grid([
    dmc.GridCol([   
        dmc.Card([
            dmc.CardSection([
                dmc.Text("titulo", size="sm")
            ], **configsCardSection),
            dmc.Text('valor', fw=500, size="lg")
        ], **configsCard)
    ], span=3),

    dmc.GridCol([   
        dmc.Card([
            dmc.CardSection([
                dmc.Text("titulo", size="sm")
            ], **configsCardSection),
            dmc.Text('valor', fw=500, size="lg")
        ], **configsCard)
    ], span=3),
], gutter="xs", align="stretch", justify='center')

## Linha 1

paper  = dict(p="xs", shadow="xl", mt="md", withBorder=True, style={'height':'100%', 'width':'100%'})

linha1 = dmc.Grid([
    dmc.GridCol([
        dmc.Paper([
            dcc.Graph(id='graph11', config=configs)
        ], **paper)
    ], span=3),
    
    dmc.GridCol([
        dmc.Paper([
            dcc.Graph(id='graph12', config=configs)
        ], **paper)
    ], span=3),
    
    dmc.GridCol([
        dmc.Paper([
            dcc.Graph(id='graph13', config=configs)
        ], **paper)
    ], span=3),
], gutter="xs", align="stretch", justify='center')


## Linha 2
paper  = dict(p="xs", shadow="xl", mt="md", withBorder=True, style={'height':'100%', 'width':'100%'})

linha2 = dmc.Grid([
    dmc.GridCol([
        dmc.Paper([
            dcc.Graph(figure=fig, config=configs)
        ], **paper)
    ], span=3),
    
    dmc.GridCol([
        dmc.Paper([
            dcc.Graph(figure=fig, config=configs)
        ], **paper)
    ], span=3),
    
    dmc.GridCol([
        dmc.Paper([
            dcc.Graph(figure=fig, config=configs)
        ], **paper)
    ], span=3),
], gutter="xs", align="stretch", justify='center')


### ------------INTERACT---------
paper2 = dict(p="xs", shadow="xs", mt="xs", withBorder=True, style={'height':'100%', 'width':'100%'})

inter = dmc.Paper([
    dmc.Grid([
        dmc.GridCol([
            dmc.MultiSelect(
                id   ="multiselect",
                label="MultiSelect",
                data=[
                    {'value': 'react', 'label': 'React'},
                    {'value': 'angular', 'label': 'Angular'},
                    {'value': 'vue', 'label': 'Vue'},
                    {'value': 'svelte', 'label': 'Svelte'},
                    ],
                value=["react"],
            )
        ], span=3),
        dmc.GridCol([
            dmc.YearPickerInput(
                minDate=datetime(2021, 1, 1),
                maxDate=datetime(2028, 1, 1),
                value=datetime(2021, 1, 1),
                placeholder="Date input",
                label="Select valid date",
                w=250,
            )
        ], span=2)


    ], gutter="xs", align="stretch", justify='center')
], **paper2)

### --------------------------

# gridStacks
stacks =  dmc.Stack([
    inter,
    linha0,
    linha1,
    linha2
], gap="xs")

# Tabs
tabs = dmc.Tabs(
    [
        dmc.TabsList(
            [
                dmc.TabsTab("Gráficos",           value="value1"),
                dmc.TabsTab("Gráficos Estaticos", value="value2"),
                dmc.TabsTab("Variados",           value="value3"),
            ]
        ),
        dmc.TabsPanel([stacks],               value="value1"),
        dmc.TabsPanel("Messages tab content", value="value2"),
        dmc.TabsPanel("Settings tab content", value="value3"),
    ],
    color="red",                # default is blue
    orientation="horizontal",   # or "vertical"
    variant="default",         # or "outline" or "pills"
    value="gallery"
)


# Callbacks
@app.callback(
    Output('graph11', 'figure'),
    Input('multiselect', 'value'),
)
def update_graph(value):
    fig = go.Figure()
    fig.update_layout(height=300)
    return fig

@app.callback(
    Output('graph12', 'figure'),
    Input('multiselect', 'value')
)       
def update_graph(value):
    fig = go.Figure()
    fig.update_layout(height=300)
    return fig

@app.callback(
    Output('graph13', 'figure'),
    Input('multiselect', 'value')
)
def update_graph(value):       
    fig = go.Figure()
    fig.update_layout(height=300)
    return fig

app.layout = dmc.MantineProvider([tabs])
if __name__ == '__main__': app.run_server(debug=True)