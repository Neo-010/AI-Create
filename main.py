import matplotlib.pyplot as plt #бібліотека для малювання графіків.
import seaborn as sns # красива обгортка над matplotlib для стильних графіків.
import pandas as pd #дуже зручна бібліотека для роботи з таблицями та даними.

df = pd.read_csv('electricity_data.csv')  # завантажує файл формату CSV (табличка, як Excel)
#скорочено від "dataframe", змінна, в якій зберігається вся таблиця
print(df.head()) #показує перші 5 рядків таблиці (щоб глянути, що там узагалі є)

X = df[['temperature', 'humidity', 'hour', 'is_weekend']] #це ті дані, за якими ми хочемо передбачити результат (наші “входи”)
y = df['consumption'] #це той стовпчик, який ми хочемо передбачити (споживання енергії)

#Тобто:
#X = температура, вологість, година, вихідний?
#y = скільки електрики реально спожито

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Тут ми ділимо дані на дві частини:

#80% — для навчання моделі (train)

#20% — для перевірки, як добре модель працює (test)
# random_state=42 — щоб розбиття було однаковим щоразу (для повторюваності)

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

# Ми створюємо лінійну модель, яка намагається "підігнати пряму" до наших даних
# .fit(...) — процес навчання: модель вивчає залежність між X і y
y_pred = model.predict(X_test)
# Тепер ми використовуємо модель, щоб передбачити значення на тих даних, які вона ще не бачила (X_test)
from sklearn.metrics import mean_absolute_percentage_error

mape = mean_absolute_percentage_error(y_test, y_pred) * 100
print(f"Середня % помилки: {mape:.2f}%")

# mean_absolute_percentage_error (MAPE) — показує, на скільки в середньому відрізняється прогноз від реальності у відсотках

plt.figure(figsize=(10, 6))
sns.scatterplot(x=y_test, y=y_pred)
plt.xlabel("Справжнє споживання")
plt.ylabel("Прогнозоване споживання")
plt.title("Справжнє vs Прогнозоване")
plt.grid(True)
plt.show()

 #Ми будуємо графік, де:

#По горизонталі — реальне споживання

#По вертикалі — прогнозоване
#Якщо модель точна, точки повинні бути близько до уявної прямої лінії (y = x)