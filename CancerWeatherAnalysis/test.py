data = [go.Scatter(
                x=df.MESS_DATUM,
                y=df['sum_meal'])]
layout = dict(
                title="timeline meal orders",
                xaxis = dict(
                type="category"))
fig = dict(data=data, layout=layout)
plot(fig, filename="overview")