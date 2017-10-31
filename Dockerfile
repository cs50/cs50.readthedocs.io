FROM cs50/server
EXPOSE 8080

RUN pip3 install raven[flask]

RUN bundle install && bundle exec jekyll build --destination /srv/www/_site
