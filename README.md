# pyramid_multistep

## What now?
Get set up for development!

```
$ pyvenv venv                              # Create Virtualenv
$ venv/bin/pip install -e.[dev]            # Install dependencies + dev dependencies
$ venv/bin/alembic upgrade head            # Run migrations
$ venv/bin/pserve development.ini --reload # Run dev server
```