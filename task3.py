import json
import matplotlib.pyplot as plt


with open('students.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


day_counts = {}
for student in data:
    day = student["day"]
    day_counts[day] = day_counts.get(day, 0) + 1


labels = list(day_counts.keys())
sizes = list(day_counts.values())


plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Розподіл учнів за днями тижня')
plt.axis('equal')  

plt.show()
