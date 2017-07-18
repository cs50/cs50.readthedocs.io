install:
	bundle install

serve: install
	bundle exec jekyll serve

build: install
	bundle exec jekyll build
