# 📈 Sales Forecasting Web App using SARIMAX

An interactive, no-code web application to forecast future sales using historical data. Built with **Streamlit**, this app allows users to upload their data, tune parameters, visualize trends, and download future predictions — all powered by the **SARIMAX** model.

---

🔗 Try It Out!


🔍 Explore the Web App: https://ecom-sales-forecast.streamlit.app/
💻 View the Code on GitHub: https://github.com/Shinnousuke/ecom-sales-forecast


---

## 📌 What This App Does

This app is designed to help businesses and analysts:
- Understand trends in past sales
- Identify seasonal patterns (e.g., festival peaks, off-season drops)
- Predict future sales using SARIMAX (a powerful time series forecasting model)

It’s perfect for anyone who wants accurate forecasts **without writing code**.

---

## ⚙️ Key Features

✅ Upload CSV file with `Date` and `Sales` columns  
✅ Customize SARIMAX parameters (`p`, `d`, `q`, `P`, `D`, `Q`, `s`) via sliders  
✅ Visualize sales trends and seasonal decompositions  
✅ Train model and view evaluation metrics (MAE, RMSE, AIC)  
✅ Display forecast with confidence intervals  
✅ Download forecast as a CSV file for reports

---

## 📊 Technologies Used

- **Python**
- **Streamlit** – UI and app framework  
- **Statsmodels** – SARIMAX forecasting  
- **Matplotlib** – Chart visualizations  
- **Pandas / NumPy** – Data handling  
- **scikit-learn** – Metrics (MAE, RMSE)

---

## 🧪 Sample Input CSV Format

```csv
Date,Sales
2022-01-01,1200
2022-02-01,1350
2022-03-01,1280
...
