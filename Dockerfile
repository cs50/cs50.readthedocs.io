FROM cs50/server
EXPOSE 8080

RUN bundle install && bundle exec jekyll build --destination /srv/www/public
