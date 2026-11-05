# Sprint_5: Автотесты для Stellar Burgers

Автотесты на Python + Selenium + pytest для сервиса [Stellar Burgers](https://stellarburgers.education-services.ru).

Проверяются: регистрация (успешная и с валидацией пароля), вход в аккаунт разными способами, переходы между конструктором и личным кабинетом, выход из аккаунта.

Покрытие: 9 автотестов — все проходят (`9 passed`).

## Структура проекта

```text
Sprint_5/
├── conftest.py                  # фикстуры: браузер, тестовые данные, залогиненный пользователь
├── requirements.txt             # зависимости
└── utils/
    ├── __init__.py
    ├── generators.py            # генераторы данных (если используются)
    └── locators.py              # локаторы элементов
└── tests/
    ├── __init__.py
    ├── test_login.py                          # вход разными способами
    ├── test_registration.py                   # регистрация и валидация пароля
    ├── test_constructor_navigation.py         # навигация по вкладкам конструктора
    └── test_profile_and_logout.py            # личный кабинет и выход
Как запустить
Создай и активируй виртуальное окружение:

Windows (PowerShell):

powershell
.\venv\Scripts\Activate.ps1
Установи зависимости:

bash
pip install -r requirements.txt
Запусти все тесты:

bash
python -m pytest -v -s
Запусти отдельный тест:

bash
python -m pytest tests/test_profile_and_logout.py::test_logout -v -s
Тестовые данные
Для входа (logged_in_driver): email и пароль жёстко прописаны в фикстуре conftest.py. Перед запуском подставь свои учётные данные (или используй тестовый аккаунт).
Для регистрации: email генерируется автоматически с уникальным суффиксом (test_user_<число>@yandex.ru) — это предотвращает ошибки «пользователь уже существует» при повторных прогонах.
Валидация пароля: для проверки ошибки используется фикстура short_password со значением "123".
Что покрыто
Файл	Тесты
test_login.py	Вход через кнопку «Войти в аккаунт» и через пункт «Личный Кабинет» в шапке
test_registration.py	Успешная регистрация; ошибка «Некорректный пароль» при коротком пароле
test_constructor_navigation.py	Переключение вкладок «Булки / Соусы / Начинки»
test_profile_and_logout.py	Переход в конструктор из ЛК, переход по логотипу, выход из аккаунта