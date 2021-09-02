	import numpy as np ## For Linear Algebra
	## For visualizations I'll be using plotly package, this creates interesting and interective visualizations.
	import plotly.express as px 
	import plotly.graph_objects as go
	from plotly.subplots import make_subplots
	from datetime import datetime ## Time Series analysis.
	df = pd.read_csv("weather.csv")
	df=pd.read_csv("weather.csv",index_col=0)
	df.head()
	print(df.head())
	df1 = pd.melt(df, id_vars='YEAR', value_vars=df.columns[1:]) ## This will melt the date
	df1['Date'] = df1['variable'] + ' ' + df1['YEAR'].astype(str)  
	df1.loc[:,'Date'] = df1['Date'].apply(lambda x : datetime.strptime(x, '%b %Y')) ## Converting String to datetime object
	df1.head()
	

	

	def timeline():
	    df1.columns=['Year', 'Month', 'Temprature', 'Date']
	    df1.sort_values(by='Date', inplace=True) ## To get the time series right.
	    fig = go.Figure(layout = go.Layout(yaxis=dict(range=[0, df1['Temprature'].max()+1])))
	    fig.add_trace(go.Scatter(x=df1['Date'], y=df1['Temprature']), )
	    fig.update_layout(title='Temprature Throught Timeline:',xaxis_title='Time', yaxis_title='Temprature in Degrees')
	    fig.update_layout(xaxis=go.layout.XAxis(
	        rangeselector=dict(
	            buttons=list([dict(label="Whole View", step="all"),
	                          dict(count=1,label="One Year View",step="year",stepmode="todate")
	                        ])),
	            rangeslider=dict(visible=True),type="date")
	    )
	    fig.show()
	

	

	

	def yearly_temp():
	    df['Yearly Mean'] = df.iloc[:,1:].mean(axis=1) ## Axis 1 for row wise and axis 0 for columns.
	    fig = go.Figure(data=[
	        go.Scatter(name='Yearly Tempratures' , x=df['YEAR'], y=df['Yearly Mean'], mode='lines'),
	        go.Scatter(name='Yearly Tempratures' , x=df['YEAR'], y=df['Yearly Mean'], mode='markers')
	    ])
	    fig.update_layout(title='Yearly Mean Temprature :',
	                 xaxis_title='Time', yaxis_title='Temprature in Degrees')
	    fig.show()
	

	def season():
	    df['Winter'] = df[['DEC', 'JAN', 'FEB']].mean(axis=1)
	    df['Summer'] = df[['MAR', 'APR', 'MAY']].mean(axis=1)
	    df['Monsoon'] = df[['JUN', 'JUL', 'AUG', 'SEP']].mean(axis=1)
	    df['Autumn'] = df[['OCT', 'NOV']].mean(axis=1)
	    seasonal_df = df[['YEAR', 'Winter', 'Summer', 'Monsoon', 'Autumn']]
	    seasonal_df = pd.melt(seasonal_df, id_vars='YEAR', value_vars=seasonal_df.columns[1:])
	    seasonal_df.columns=['Year', 'Season', 'Temprature']
	

	    fig = px.scatter(seasonal_df, 'Year', 'Temprature', facet_col='Season', facet_col_wrap=2, trendline='ols')
	    fig.update_layout(title='Seasonal mean tempratures throught years:')
	    fig.show()
	yearly_temp()

