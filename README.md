# Codeleap Challenge

This API was developed to solve a coding challenge suggested by CodeLeap.

## Run locally

```bash
python3 -m venv env
source env/bin/activate
pip install djangorestframework

cd api
python .\manage.py runserver
```

## Endpoints

#### List all posts

```http
GET http://localhost:8000/careers/
```

```json
[
    {
        "id": 1,
        "username": "GabrielSpacki",
        "created_datetime": "2024-02-29T05:14:38.528455Z",
        "title": "My First Post",
        "content": "Hello, World!"
    },
    {
        "id": 2,
        "username": "LauraSilvestrin",
        "created_datetime": "2024-02-29T05:15:03.986621Z",
        "title": "Hey!!",
        "content": "Hello, Everyone!"
    },
    {
        "id": 3,
        "username": "LauraSilvestrin",
        "created_datetime": "2024-02-29T05:15:59.723869Z",
        "title": "Hey!!",
        "content": "fixed!"
    },
]
```

#### Create a new post

```http
POST http://localhost:8000/careers/
```

Input

```json
  {
    "username": "GabrielSpacki",
    "title": "Example of a new post!",
    "content": "Type something nice here :)"
  },
```

Output

```json
  {
    "id": 1,
    "username": "GabrielSpacki",
    "created_datetime": "2024-02-29T05:14:38.528455Z",
    "title": "Example of a new post!",
    "content": "Type something nice here :)"
  },
```

#### Update post

```http
PATCH http://localhost:8000/careers/${id}/
```

| Parameter | Type     | Description                                            |
| :-------- | :------- | :------------------------------------------------------|
| `id`      | `integer` | **Mandatory**. The ID of the post that you're updating |

Input

```json
  {
    "title": "Example of a new post! (Updated)",
    "content": "Type something great here :)"
  },
```

Output

```json
  {
    "id": 1,
    "username": "GabrielSpacki",
    "created_datetime": "2024-02-29T05:14:38.528455Z",
    "title": "Example of a new post! (Updated)",
    "content": "Type something great here :)"
  },
```

#### Delete post

```http
DELETE http://localhost:8000/careers/${id}/
```

| Parameter | Type     | Description                                            |
| :-------- | :------- | :------------------------------------------------------|
| `id`      | `integer` | **Mandatory**. The ID of the post that you're updating |

Output

```json
{}
```


This API was developed to solve a coding challenge suggested by CodeLeap. It simulates a CRUD of posts inside a social network