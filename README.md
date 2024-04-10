# Проект Управления Палитрами и Цветами
 Проект предоставляет REST API для управления палитрами и цветами, включая регистрацию и аутентификацию пользователей, работу с палитрами и цветами. Пользователи могут создавать, изменять, просматривать и удалять собственные палитры и цвета. Имена цветов генерируются автоматически на основе HEX-кода с использованием The Color API.

## Технологический стек
- Django REST Framework
- PostgreSQL для базы данных
- Docker для контейнеризации и упрощения развертывания
- drf-spectacular для Swagger документации API

# Установка и запуск
- Установите Docker и Docker Compose для вашей операционной системы.

# Шаги для запуска
- Клонируйте репозиторий: git clone https://github.com/Stanis4live/RuYou-test-project-Stanislav-Bobovych
- cd RuYou-test-project-Stanislav-Bobovych
- Запустите проект с помощью Docker Compose: docker-compose up --build
- После запуска сервер доступен по адресу http://localhost:8000/

# Работа с API
Для просмотра доступных эндпоинтов и их документации посетите 
- Swagger UI по адресу http://localhost:8000/api/schema/swagger-ui/
- Redoc по адресу http://localhost:8000/api/schema/redoc/

# Основные эндпоинты API
# Аутентификация
- Регистрация пользователя: POST /user/signup/
- Вход пользователя: POST /user/login/
# Палитры
CRUD операции с палитрами: /palettes/
- Создание палитры: POST /palettes/
- Получение списка палитр: GET /palettes/
- Получение деталей палитры: GET /palettes/{id}/
- Обновление палитры: PUT /palettes/{id}/ или PATCH /palettes/{id}/
- Удаление палитры: DELETE /palettes/{id}/
# Цвета
CRUD операции с цветами: /colors/
- Создание цвета: POST /colors/ (с указанием palette_id в теле запроса)
- Получение списка цветов по палитре: GET /colors/?palette_id={palette_id}
- Получение деталей цвета: GET /colors/{id}/
- Обновление цвета: PATCH /colors/{id}/
- Удаление цвета: DELETE /colors/{id}/



