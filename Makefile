install:
	bundle install

serve: install
	bundle exec jekyll serve --host=0.0.0.0 --incremental --port=8080

build: install
	bundle exec jekyll build
