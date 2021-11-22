#  anchor-python-sphinx

Common documentation configuration routine for Anchor Python projects.

See [Anchor image analysis](https://www.anchoranalysis.org/) and associated [GitHub projects](https://github.com/anchoranalysis/).

## Usage

1.	Place a dependency to `anchor_python_sphinx` in the docs/requirements.txt (or equivalent) in the project to    be documented. e.g.

	```
	git+https://github.com/anchoranalysis/anchor-python-sphinx.git#egg=anchor_python_sphinx
	```

2.	Create or change the `docs/conf.py` to be similar to:


	```python
	from anchor_python_sphinx import configure_sphinx
	
	
	# Importing Sphinx settings from the anchor_python_sphinx library
	def setup(app):
	    configure_sphinx.configure(app, "name_of_project", version="2.1", author="John Doe")
```

3. Optionally, create a file 'docs/_static/custom.css' which will modify the default Read-the-Docs stylesheet to allow content spread more widely across the page.

	```
	.wy-nav-content {
	    max-width: 75% !important;
	}
	```

4. Generate the Sphinx documentation in the usual way by e.g. `make html` in the `docs` subdirectory, or by `tox -e docs`.


## Author

Owen Feehan

## License

[MIT](LICENSE)
