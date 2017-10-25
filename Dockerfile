FROM cs50/server:passenger-5.1.11
EXPOSE 8080

RUN pip3 install raven[flask]

RUN bundle install && bundle exec jekyll build --destination /srv/www/_site
