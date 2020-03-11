import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels.api as sm

df = pd.read_csv('health.csv')
model = sm.OLS.from_formula("points ~ workout",data=df)
result = model.fit()
result.summary()

# correlation between two entities
r = df['workout'].corr(df['points'])
print(r)
# Regression plot
sns.regplot(y="points",x="workout",data = df)
