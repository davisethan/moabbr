.PHONY: docs
docs:
	rm -rf docs
	sphinx-build -b html sphinx docs
	touch docs/.nojekyll

.PHONY: publish
publish:
	rm -rf dist
	python -m build
	twine upload dist/*
