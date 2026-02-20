from product import ProductCard


def edit_product(product) -> None:
    """Функция для изменения информации о продукте."""

    print("\n=== Изменение товара ===")
    print("1. Название")
    print("2. Количество")
    print("3. Состояние")
    print("4. Цена")
    print("5. Вес")
    print("6. Объем")

    choice = input("Выберите поле: ")

    if choice == "1":
        product.name = input("Новое название: ")

    elif choice == "2":
        product.quantity = input("Новое количество: ")

    elif choice == "3":
        product.state = input("Новое состояние: ")

    elif choice == "4":
        product.price = input("Новая цена: ")

    elif choice == "5":
        product.weight = input("Новый вес: ")

    elif choice == "6":
        product.volume = input("Новый объем: ")


def main() -> None:
    """Основная функция меню."""
    product = ProductCard(
        name="Toy1",
        quantity=10,
        state="Не поступил",
        importer="ToyCorp",
        manufacturer="Factory",
        price=100.0,
        origin_country="China",
        composition="Plastic",
        weight=0.5,
        volume=0.2
    )

    in_work = True

    while in_work:
        print("=== Меню ===")
        print("1. Показать карточку")
        print("2. Изменить карточку")
        print("3. Списать товар")
        print("4. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            print(product)

        elif choice == "2":
            edit_product(product)

        elif choice == "3":
            product.state = "Списано"

        elif choice == "4":
            print("Выход из программы.")
            in_work = False

        else:
            print("Некорректный выбор.\n")


if __name__ == "__main__":
    main()
