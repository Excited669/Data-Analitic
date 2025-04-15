import matplotlib.pyplot as plt

n = int(input("Введите число "))
x_values = list(range(1,n))
y_values = [x**3 for x in x_values]

plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.scatter(x_values,y_values, c = "red", cmap=plt.cm.Greens, s = 10)

ax.set_title('Square Numbers', fontsize = 24)
ax.set_xlabel('Value', fontsize = 14)
ax.set_ylabel('Square of Value', fontsize = 14)

plt.show()