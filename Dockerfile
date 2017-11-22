FROM cs50/server:ubuntu
EXPOSE 8080

RUN pip3 install raven[flask]

RUN bundle install && bundle exec jekyll build --destination /var/www/_site
