class ProductCard:
    """
    Класс, представляющий карточку товара на складе.
    """

    def __init__(
            self,
            name: str,
            quantity: int,
            state: str,
            importer: str,
            manufacturer: str,
            price: int | float,
            origin_country: str,
            composition: str,
            weight: int | float,
            volume: int | float
    ) -> None:
        """
        Инициализирует объект карточки товара.

        Args:
            name: Название товара.
            quantity: Количество единиц на складе.
            state: Текущее состояние (например, 'Поступил', 'Списано').
            importer: Организация-импортер.
            manufacturer: Компания-производитель.
            price: Цена за единицу товара.
            origin_country: Страна производства.
            composition: Состав или материалы.
            weight: Вес товара.
            volume: Объем товара.
        """

        self._state = None
        self.name = name
        self.quantity = quantity
        self.state = state
        self.importer = importer
        self.manufacturer = manufacturer
        self.price = price
        self.origin_country = origin_country
        self.composition = composition
        self.weight = weight
        self.volume = volume

    @property
    def name(self) -> str:
        """Возвращает название товара."""

        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """
        Устанавливает название товара с проверкой типа.

        Raises:
            TypeError: Если значение не является строкой.
        """

        try:
            if not isinstance(value, str):
                raise TypeError("Название должно быть строкой")

            self._name = value

        except TypeError as e:
            print(f"Ошибка: {e}")

    @property
    def quantity(self) -> int:
        """Возвращает количество товара."""

        return self._quantity

    @quantity.setter
    def quantity(self, value: int) -> None:
        """
        Устанавливает количество товара с проверкой на тип и отрицательное значение.

        Raises:
            TypeError: Если значение не является целым числом.
            ValueError: Если значение отрицательное.
        """

        try:
            if not isinstance(value, int):
                raise TypeError("Количество должно быть целым числом")

            if value < 0:
                raise ValueError("Количество товара не может быть отрицательным")

            self._quantity = value

        except (ValueError, TypeError) as e:
            print(f"Ошибка: {e}")

    @property
    def state(self) -> str | None:
        """Возвращает текущее состояние товара."""

        return self._state

    @state.setter
    def state(self, value: str) -> None:
        """
        Устанавливает состояние товара с проверкой логики переходов.

        Raises:
            TypeError: Если значение не является строкой.
            ValueError: Если нарушена логика смены состояния.
        """

        try:
            if not isinstance(value, str):
                raise TypeError("Состояние должно быть строкой")

            if value == "Списано" and self._state != "Поступил":
                raise ValueError("Товар ещё не поступил на склад")

            elif self._state == "Списано":
                raise ValueError("Товар уже списан")

            self._state = value

        except (ValueError, TypeError) as e:
            print(f"Ошибка: {e}")

    @property
    def importer(self) -> str:
        """Возвращает название импортера."""

        return self._importer

    @importer.setter
    def importer(self, value: str) -> None:
        """
        Устанавливает название импортера.

        Raises:
            TypeError: Если значение не является строкой.
        """

        try:
            if not isinstance(value, str):
                raise TypeError("Импортер должен быть строкой")

            self._importer = value

        except TypeError as e:
            print(f"Ошибка: {e}")

    @property
    def manufacturer(self) -> str:
        """Возвращает название производителя."""

        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, value: str) -> None:
        """
        Устанавливает название производителя.

        Raises:
            TypeError: Если значение не является строкой.
        """

        try:
            if not isinstance(value, str):
                raise TypeError("Производитель должен быть строкой")

            self._manufacturer = value

        except TypeError as e:
            print(f"Ошибка: {e}")

    @property
    def price(self) -> int | float:
        """Возвращает цену товара."""

        return self._price

    @price.setter
    def price(self, value: int | float) -> None:
        """
        Устанавливает цену товара с проверкой на положительное число.

        Raises:
            TypeError: Если значение не является числом.
            ValueError: Если значение неположительное.
        """

        try:
            if not isinstance(value, (int, float)):
                raise TypeError("Цена должна быть числом")

            if value <= 0:
                raise ValueError("Цена должна быть положительной")

            self._price = value

        except (ValueError, TypeError) as e:
            print(f"Ошибка: {e}")

    @property
    def origin_country(self) -> str:
        """Возвращает страну происхождения."""

        return self._origin_country

    @origin_country.setter
    def origin_country(self, value: str) -> None:
        """
        Устанавливает страну происхождения.

        Raises:
            TypeError: Если значение не является строкой.
        """

        try:
            if not isinstance(value, str):
                raise TypeError("Страна происхождения должна быть строкой")

            self._origin_country = value

        except TypeError as e:
            print(f"Ошибка: {e}")

    @property
    def composition(self) -> str:
        """Возвращает состав товара."""

        return self._composition

    @composition.setter
    def composition(self, value: str) -> None:
        """
        Устанавливает состав товара.

        Raises:
            TypeError: Если значение не является строкой.
        """

        try:
            if not isinstance(value, str):
                raise TypeError("Состав должен быть строкой")

            self._composition = value

        except TypeError as e:
            print(f"Ошибка: {e}")

    @property
    def weight(self) -> int | float:
        """Возвращает вес товара."""

        return self._weight

    @weight.setter
    def weight(self, value: int | float) -> None:
        """
        Устанавливает вес товара с проверкой на положительное число.

        Raises:
            TypeError: Если значение не является числом.
            ValueError: Если значение неположительное.
        """

        try:
            if not isinstance(value, (int, float)):
                raise TypeError("Вес должен быть числом")

            if value <= 0:
                raise ValueError("Вес должен быть положительным числом")

            self._weight = value

        except (ValueError, TypeError) as e:
            print(f"Ошибка: {e}")

    @property
    def volume(self) -> int | float:
        """Возвращает объем товара."""

        return self._volume

    @volume.setter
    def volume(self, value: int | float) -> None:
        """
        Устанавливает объем товара с проверкой на положительное число.

        Raises:
            TypeError: Если значение не является числом.
            ValueError: Если значение неположительное.
        """

        try:
            if not isinstance(value, (int, float)):
                raise TypeError("Объем должен быть числом")

            if value <= 0:
                raise ValueError("Объём должен быть положительным числом")

            self._volume = value

        except (ValueError, TypeError) as e:
            print(f"Ошибка: {e}")

    def __str__(self) -> str:
        """
        Возвращает полную информацию о товаре.
        """

        return (
            f"\n--- Карточка товара ---\n"
            f"Название: {self.name}\n"
            f"Количество: {self.quantity}\n"
            f"Состояние: {self.state}\n"
            f"Импортер: {self.importer}\n"
            f"Производитель: {self.manufacturer}\n"
            f"Цена: {self.price}\n"
            f"Страна происхождения: {self.origin_country}\n"
            f"Состав: {self.composition}\n"
            f"Вес: {self.weight}\n"
            f"Объем: {self.volume}\n"
        )
