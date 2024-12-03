import random
import matplotlib.pyplot as plt
import tkinter as tk




def run_program():

    random_numbers = [random.randint(500, 1000000) for _ in range(30)]


    numbers_below_10000 = [num for num in random_numbers if num < 10000]


    total_sum = sum(random_numbers)


    print("Všetky hodnoty:")
    print(random_numbers)
    print("\nHodnoty menšie ako 10 000:")
    print(numbers_below_10000)
    print(f"\nSúčet všetkých hodnôt: {total_sum}")


    plt.figure(figsize=(12, 6))
    plt.bar(range(len(random_numbers)), random_numbers, color='lightblue', edgecolor='black')
    plt.title("Graf všetkých hodnôt")
    plt.xlabel("Index")
    plt.ylabel("Hodnota")
    plt.xticks(range(len(random_numbers)))
    plt.grid(axis='y', linestyle='--', alpha=0.7)


    plt.gcf().text(
        0.1,
        0.95,
        f"Súčet hodnôt: {total_sum}", fontsize=12, color='black', ha='center', va='top'
    )

    plt.show()



root = tk.Tk()
root.title("Moje Zadanie")


label = tk.Label(
    root,
    text="Predmet:Programovacie tachniky\nMeno: Dávid Zlatohlavý\nZadanie: 25",
    font=("Arial", 12),
    justify="center"
)
label.pack(pady=20)


button = tk.Button(
    root,
    text="Stlač ma",
    font=("Arial", 14),
    command=run_program,
    bg="lightblue",
    fg="black"
)
button.pack(pady=10)


root.mainloop()

