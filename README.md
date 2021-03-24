# GALLERYA

A Gallery app built on Django with a robust backend for adding photos, a search function and sorts images by categories

## Getting Started

- clone this repo

```
$ git clone https://github.com/BwanaQ/galleria.git
```

### Prerequisites

- Python 3 latest version
- Pip3 installer
- virtualenv command

### Installing

1. cd into the galleria folder

```
$ cd galleria
```

2. Add a python 3 environment

```
$ virtualenv env
```

3. Enter the virtual environment

```
$ source env/bin/activate
```

4. Install dependanies from requirements.txt

```
(env)$ pip install -r requirements.txt
```

5. rename .env copy to .env then run this command

```
(env) $ source .env
```

6. Run server

```
(env) $ python manage.py runserver
```

## Deployment

to deploy to heroku simply create a project, attach your git hub repository and

## Built With

- [Django](https://www.djangoproject.com/) - The web framework used
- [Bootstrap](https://getbootstrap.com/) - Frontend for the monolithic app

## Authors

- **Tom Hunja**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

- Thanks to [Toptal](https://www.toptal.com/developers/gitignore/api/django) for a beautiful .gitignore file
- Inspiration - My Technical Mentor Kelvin Onkundi and The Olympians Team MC38
