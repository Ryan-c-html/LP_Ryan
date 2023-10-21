# Importando a biblioteca principal
import pandas as pd

# Questão 1---------------

# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruits.
fruits = pd.DataFrame({'Apples': [30], 'Bananas': [21]})

# Check your answer
print(fruits)
print('\n---------------------------------------------------------\n')
# Questão 2---------------

# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruit_sales.
fruit_sales = pd.DataFrame({'Apples': [35, 41], 'Bananas': [21, 34]}, index=['2017 Sales', '2018 Sales'])

# Check your answer
print(fruit_sales)
print('\n---------------------------------------------------------\n')
# Questão 3----------------

ingredients = pd.Series(['4 cups', '1 cup', '2 large', '1 can'], index=['Flour', 'Milk', 'Eggs', 'Spam'], name='Dinner')

# Check your answer
print(ingredients)
print('\n---------------------------------------------------------\n')

