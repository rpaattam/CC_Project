import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from matplotlib import style
import random

import datetime as dt
import pandas_datareader.data as web
import mplfinance as mpf
from finquant.portfolio import build_portfolio
import yfinance

style.use('ggplot')


def app():
    uploaded_file = st.file_uploader("Choose a file: ", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        # uploaded_file.get()
        # df = pd.read_excel('materials.xlsx', nrows=nrows)

        st.dataframe(df)

        Portfolio_Total_Amount = sum(df['Allocation'] * df['Average_Price'])
        Portfolio_Total_Amount = round(Portfolio_Total_Amount, 2)
        st.write(Portfolio_Total_Amount)

        stock_tickers = df['Name'].values
        sizes = df['Allocation'] * df['Average_Price']

        listOfZeros = [0] * df.shape[0]
        n = random.randint(0, df.shape[0] - 1)
        listOfZeros[n] = 0.1
        explode = listOfZeros

        # Create a figure
        '''
        fig1, ax1 = plt.subplots(figsize=(10, 10))
        ax1.pie(sizes, explode=explode, labels=stock_tickers, autopct='%.2f%%', shadow='True', startangle=360)
        ax1.set_title('Portfolio Pie Chart', color='Purple', fontsize=22)


        # modified pyplot

        fig2, ax2 = plt.subplots(figsize=(10, 10))
        plt.pie(sizes, labels=stock_tickers, startangle=90, frame=True, explode=explode, radius=3)
        plt.pie(sizes, startangle=90, radius=2)
        # Draw circle
        centre_circle = plt.Circle((0, 0), 1.5, color='black', fc='white', linewidth=0)
        fig2 = plt.gcf()
        fig2.gca().add_artist(centre_circle)
        plt.axis('equal')
        plt.tight_layout()
        '''

        # plotly graph
        # fig = make_subplots(rows=1, cols=2)
        fig = px.pie(df, values=sizes, names=stock_tickers, title='Portfolio Pie Chart', width=200, height=200,
                     color_discrete_sequence=px.colors.sequential.RdBu)
        fig.update_traces(textposition='inside', textinfo='percent+label',
                          marker=dict(line=dict(color='#000000', width=1)))
        # fig.update_layout()
        # fig.show()

        '''
        x = -1.75
        y = 1
        ax1.text(x, y, 'Overview:', fontsize=24, color='Purple')

        y_counter = 0.12

        ax1.text(x, y - y_counter, 'Total: ' + str(Portfolio_Total_Amount), fontsize=15, color='Blue')

        for i in range(0, df.shape[0]):
            ax1.text(x, 0.88 - y_counter,
                     df['Name'][i] + ': $' + str(round(df['Allocation'][i] * df['Average_Price'][i], 3)),
                     fontsize=14, color='Black')
            y_counter = y_counter + 0.12

         '''

        # st.pyplot(fig1)
        # st.pyplot(fig)
        st.plotly_chart(fig)

        ##### Portfolio

        df_1 = df[['Name', 'Allocation']]
        pf_allocation = df_1
        pf_allocation

        names = df_1["Name"].values.tolist()
        names

        start_date = dt.datetime(2015, 1, 1)
        end_date = dt.datetime.now()

        pf = build_portfolio(names=names, pf_allocation=pf_allocation, start_date=start_date, end_date=end_date,
                             data_api='yfinance')

        st.write(pf.portfolio)
        # print(pf.data.head(3))
        # print(pf)
        pf_1 = pf.expected_return
        st.write(pf_1)

        pf_fig = pf.comp_cumulative_returns().plot().axhline(y=0, color="black", lw=3)

        # st.pyplot(pf_fig)

        ##### Individual Graphs
        data = df

        start = dt.datetime(2020, 1, 1)
        end = dt.datetime.now()
        for i in data['Name']:
            df = web.DataReader(i, 'yahoo', start, end)
            df.to_csv(i + '.csv')

            st.write(i)

            daily_1 = pd.read_csv(i + '.csv', index_col=0, parse_dates=True)

            daily_1.index.name = 'Date'
            daily_1.shape
            daily_1.head(3)
            daily_1.tail(3)

            st.set_option('deprecation.showPyplotGlobalUse', False)

            plot_a1 = mpf.plot(daily_1)
            st.pyplot(plot_a1)

            plot_a2 = mpf.plot(daily_1, type='candle', mav=(3, 6, 9), volume=True)
            st.pyplot(plot_a2)
