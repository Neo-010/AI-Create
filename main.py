import pandas as pd

# 1. Створити DataFrame та конвертувати колонку OrderDate у datetime
data = {
    'OrderID': [1001, 1002, 1003],
    'Customer': ['Alice', 'Bob', 'Alice'],
    'Product': ['Laptop', 'Chair', 'Mouse'],
    'Category': ['Electronics', 'Furniture', 'Electronics'],
    'Quantity': [1, 2, 3],
    'Price': [1500, 180, 25],
    'OrderDate': ['2023-06-01', '2023-06-03', '2023-06-05']
}

df = pd.DataFrame(data)
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

# 2. Додати стовпець TotalAmount
df['TotalAmount'] = df['Quantity'] * df['Price']

# 3a. Сумарний дохід магазину
total_income = df['TotalAmount'].sum()

# 3b. Середнє значення TotalAmount
average_total = df['TotalAmount'].mean()

# 3c. Кількість замовлень по кожному клієнту
orders_per_customer = df['Customer'].value_counts()

# 4. Замовлення, в яких сума покупки перевищує 500
high_value_orders = df[df['TotalAmount'] > 500]

# 5. Відсортувати за OrderDate у зворотному порядку
sorted_df = df.sort_values(by='OrderDate', ascending=False)

# 6. Замовлення з 5 по 10 червня включно
june_orders = df[(df['OrderDate'] >= '2023-06-05') & (df['OrderDate'] <= '2023-06-10')]

# 7. Групування по категорії
grouped = df.groupby('Category').agg({
    'Quantity': 'sum',
    'TotalAmount': 'sum'
}).reset_index()

# 8. ТОП-3 клієнтів за загальною сумою покупок
top_customers = df.groupby('Customer')['TotalAmount'].sum().sort_values(ascending=False).head(3)

# Вивід результатів
print("\n\n\nСумарний дохід:\n\n\n", total_income)
print("\n\n\nСередній TotalAmount:\n\n\n", average_total)
print("\n\n\nКількість замовлень по клієнтах:\n\n\n", orders_per_customer)
print("\n\n\nЗамовлення з TotalAmount > 500:\n\n\n", high_value_orders)
print("\n\n\nВідсортована таблиця за датою (спадання):\n\n\n", sorted_df)
print("\n\n\nЗамовлення з 5 по 10 червня включно:\n\n\n", june_orders)
print("\n\n\nГрупування за категорією:\n\n\n", grouped)
print("\n\n\nТОП-3 клієнтів за сумою покупок:\n\n\n", top_customers)
