import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.seasonal import seasonal_decompose
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

st.title("📈 Sales Forecasting App")

# Sidebar - Parameter tuning
st.sidebar.header("🔧 SARIMAX Parameters")
p = st.sidebar.slider("p (AR)", 0, 5, 1)
d = st.sidebar.slider("d (Differencing)", 0, 2, 1)
q = st.sidebar.slider("q (MA)", 0, 5, 1)
P = st.sidebar.slider("P (Seasonal AR)", 0, 3, 1)
D = st.sidebar.slider("D (Seasonal Diff)", 0, 2, 1)
Q = st.sidebar.slider("Q (Seasonal MA)", 0, 3, 1)
s = st.sidebar.selectbox("Season Length (s)", [6, 12, 24], index=1)

# File Upload
uploaded_file = st.file_uploader("📤 Upload CSV with 'Date' and 'Sales' columns", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    try:
        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index('Date', inplace=True)
        df = df.sort_index()
        st.success("✅ File loaded successfully.")

        st.write("📊 Sample Data")
        st.write(df.head())

        # Plot original data
        st.subheader("📈 Sales Over Time")
        fig, ax = plt.subplots()
        df['Sales'].plot(ax=ax)
        ax.set_title("Historical Sales Data")
        st.pyplot(fig)

        # Forecasting period
        steps = st.slider("📆 Select number of months to forecast", 1, 24, 6)

        # Train SARIMAX
        st.subheader("🔁 SARIMAX Model Training...")
        model = SARIMAX(df['Sales'], order=(p, d, q), seasonal_order=(P, D, Q, s))
        results = model.fit(disp=False)
        st.success("🎉 Model training complete.")

        # Model Evaluation
        train_preds = results.fittedvalues
        mae = mean_absolute_error(df['Sales'][1:], train_preds[1:])
        rmse = np.sqrt(mean_squared_error(df['Sales'][1:], train_preds[1:]))

        st.subheader("📊 Model Evaluation Metrics")
        st.metric("MAE", f"{mae:.2f}")
        st.metric("RMSE", f"{rmse:.2f}")
        st.write("AIC:", round(results.aic, 2))

        # Residual Plot
        st.subheader("🔍 Residual Plot")
        residuals = df['Sales'] - train_preds
        fig_resid, ax_resid = plt.subplots()
        residuals.plot(ax=ax_resid)
        ax_resid.set_title("Model Residuals")
        st.pyplot(fig_resid)

        # Decomposition
        st.subheader("📉 Seasonal Decomposition")
        try:
            decomp = seasonal_decompose(df['Sales'], model='additive', period=s)
            fig_decomp = decomp.plot()
            st.pyplot(fig_decomp)
        except:
            st.warning("⚠️ Not enough data points for seasonal decomposition.")

        # Forecasting
        forecast = results.get_forecast(steps=steps)
        forecast_index = pd.date_range(df.index[-1] + pd.offsets.MonthBegin(), periods=steps, freq='MS')
        forecast_df = pd.DataFrame({
            'Forecast': forecast.predicted_mean,
            'Lower CI': forecast.conf_int().iloc[:, 0],
            'Upper CI': forecast.conf_int().iloc[:, 1]
        }, index=forecast_index)

        # Forecast Plot
        st.subheader("📈 Forecasted Sales")
        fig2, ax2 = plt.subplots()
        df['Sales'].plot(ax=ax2, label='Historical')
        forecast_df['Forecast'].plot(ax=ax2, label='Forecast')
        ax2.fill_between(forecast_df.index, forecast_df['Lower CI'], forecast_df['Upper CI'], color='gray', alpha=0.3)
        ax2.legend()
        ax2.set_title("Sales Forecast with SARIMAX")
        st.pyplot(fig2)

        # Forecast Table
        st.subheader("📋 Forecasted Values")
        st.write(forecast_df)

        # Download CSV
        csv = forecast_df.to_csv().encode('utf-8')
        st.download_button("⬇️ Download Forecast CSV", csv, "forecast.csv", "text/csv")

    except Exception as e:
        st.error("❌ Error: Check your data format. Expected 'Date' and 'Sales' columns.")
        st.exception(e)
