sudo apt-get install ruby`ruby -e 'puts RUBY_VERSION[/\d+\.\d+/]'`-dev
sudo gem install jekyll bundler
mkdir blog && cd blog
bundler init
nano Gemfile // add gem 'jekyll'
sudo gem install eventmachine -v '1.2.7' --source 'https://rubygems.org/'
jekyll build
bundle exec jekyll build
bundle exec jekyll serve --watch
