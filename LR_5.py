introduction = input("Якщо хочете дізнатися, як працює програма, то напишіть (так/ні): ")
if introduction == "так":
    print("Програма виводить результат загальної вартості всіх товарів зі списку.")
else:
    print("Тоді почнемо!")
def calculate_total_cost(file_path):
    total_cost = 0.0
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Розділити рядок на назву товару та вартість за допомогою '--'
                parts = line.strip().split(' -- ')
                
                # Перевірка, чи вдалося розділити рядок на дві частини
                if len(parts) == 2:
                    # Отримати вартість та додати її до загальної вартості
                    cost = float(parts[1])
                    total_cost += cost
                else:
                    print(f"Помилка у рядку: {line}. Перевірте формат.")

    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")

    return total_cost

# Приклад виклику функції
file_path = 'C:\\Users\\NAZ\\Desktop\\python_work\\file_path.txt'
result = calculate_total_cost(file_path)
print(f"Загальна вартість всіх товарів: {result}")
