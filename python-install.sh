sudo apt-get update \
  && sudo apt-get install -y build-essential git libexpat1-dev libssl-dev zlib1g-dev \
  libncurses5-dev libbz2-dev liblzma-dev \
  libsqlite3-dev libffi-dev tcl-dev libgdbm-dev \
  libreadline-dev tk tk-dev

  git clone https://github.com/python/cpython.git
  cd cpython && ./configure --prefix=/usr \
  --enable-loadable-sqlite-extensions \
  --enable-shared \
  --with-lto \
  --enable-optimizations \
  --with-system-expat \
  --with-system-ffi \
  --enable-ipv6 --with-threads --with-pydebug --disable-rpath \
  && make \
  && sudo make install
