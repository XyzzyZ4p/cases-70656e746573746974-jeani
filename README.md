# jeani

Написать Python-скрипт, который преобразует входящий JSON
в список с уникальными элементами. Учесть, что в JSON
может быть большой уровень вложенности. JSON необходимо
загружать из файла, путь к которому предаётся в аргументах
запуска скрипта.

Исходный JSON:

        {
            "Users": [
                {
                    "id": 1,
                    "employee": {
                        "department": "tech",
                        "name": "Mark",
                        "project": [
                            {
                                "id": 2,
                                "name": "Test",
                                "status": "ok",
                                "mistakes": []
                            }
                        ]
                    }
                },
                {
                    "id": 2,
                    "employee": {
                        "department": "tech",
                        "name": "Alex",
                        "project": [
                            {
                                "id": 3,
                                "name": "parser",
                                "status": "filed",
                                "mistakes": [404, "IO error"]
                            }
                        ]
                    }
                }
            ]
        }

Результат (порядок необязателен):

        [
            'Users',
            'id',
            1,
            'employee',
            'department',
            'tech',
            'name',
            'Mark',
            'project',
            2,
            'Test',
            'status',
            "ok",
            'mistakes',
            'Alex',
            3,
            'parser',
            'filed',
            404,
            'IO error'
        ]

## Build

        poetry install
        poetry build
        python3 -m pip install --user dist/jeani-0.1.0-none-any.whl

## Using

        python3 -m jeani [OPTIONS] [JSON_PATH]

        Options:
            --help  Show this message and exit.
        
        * script is compatible with PIPE

## Testing

        poetry install --with=dev
        pytest
