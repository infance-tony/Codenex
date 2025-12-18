import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.stats.anova import anova_lm
from statsmodels.robust import mad
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.stattools import omni_normtest, jarque_bera, durbin_watson
from statsmodels.tsa.holtwinters import ExponentialSmoothing

import statsmodels.api as sm
import statsmodels.formula.api as smf

# Sample data for regression
np.random.seed(42)
n = 100
X = np.random.randn(n, 2)
X = sm.add_constant(X)
y = 2 + 3*X[:,1] + 4*X[:,2] + np.random.randn(n)

# Linear Regression (OLS)
ols_model = sm.OLS(y, X).fit()
print("OLS Summary:")
print(ols_model.summary())
print("Coefficients:", ols_model.params)
print("Confidence Intervals:", ols_model.conf_int())

# Logistic Regression (using binary y)
y_binary = (y > np.median(y)).astype(int)
logit_model = sm.Logit(y_binary, X).fit()
print("\nLogit Summary:")
print(logit_model.summary())

# GLM
glm_model = sm.GLM(y, X, family=sm.families.Gaussian()).fit()
print("\nGLM Summary:")
print(glm_model.summary())

# Time Series: ARIMA
ts_data = np.random.randn(100)
arima_model = ARIMA(ts_data, order=(1,1,1)).fit()
print("\nARIMA Summary:")
print(arima_model.summary())

# SARIMAX
sarimax_model = SARIMAX(ts_data, order=(1,1,1), seasonal_order=(1,1,1,12)).fit()
print("\nSARIMAX Summary:")
print(sarimax_model.summary())

# ANOVA (using formula API)
df = pd.DataFrame({'y': y, 'group': np.random.choice(['A', 'B', 'C'], n)})
anova_model = smf.ols('y ~ group', data=df).fit()
anova_table = anova_lm(anova_model)
print("\nANOVA Table:")
print(anova_table)

# Mixed Linear Models (simple example)
mixed_model = smf.mixedlm('y ~ X1', data=pd.DataFrame({'y': y, 'X1': X[:,1], 'group': np.random.choice(['G1', 'G2'], n)}), groups='group').fit()
print("\nMixedLM Summary:")
print(mixed_model.summary())

# Descriptive Statistics
print("\nDescriptive Stats:")
print("Mean:", np.mean(y))
print("Median:", np.median(y))
print("Variance:", np.var(y))
print("Robust Kurtosis:", sm.robust.kurtosis(y))
print("Robust Skewness:", sm.robust.skewness(y))

# Hypothesis Testing
# Breusch-Pagan Test
bp_test = het_breuschpagan(ols_model.resid, ols_model.model.exog)
print("\nBreusch-Pagan Test:", bp_test)

# Normality Tests
omni_test = omni_normtest(ols_model.resid)
print("Omni Normtest:", omni_test)
jb_test = jarque_bera(ols_model.resid)
print("Jarque-Bera Test:", jb_test)
dw_test = durbin_watson(ols_model.resid)
print("Durbin-Watson Test:", dw_test)

# Exponential Smoothing
es_model = ExponentialSmoothing(ts_data).fit()
print("\nExponential Smoothing Forecast:")
print(es_model.forecast(5))