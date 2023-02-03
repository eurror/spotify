# Spotify clone app

This app is a music app which lets you play your favorite songs right from your pocket (NO)
## Installation

```bash
mkdir foo && cd foo
python3 -m venv <venv_name>
. venv/bin/activate
git clone https://github.com/eurror/spotify
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install -r requirements.txt
```
Now create dotenv file (.env) and fill in your database (we use PostgreSQL) name, username and password

After you're done setting up everything, run a make command to run a local server.
```bash
make run #or
python manage.py runserver
```

## Contributing

Fell free to pull request. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
