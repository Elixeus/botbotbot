###### pocketsphinx & sphinxbase  

```bash
# Download
# https://cmusphinx.github.io/wiki/download/
	# sphinxbase-5prealpha
	# pocketsphinx-5prealpha
		# make sure sphinxbase and pocketsphinx versions are in sync
	# Model - Language - Dictionary
	
# Install
# Change current directory to sphinxbase folder
./autogen.sh
./configure
make
[sudo] make install 
# The sphinxbase will be installed in /usr/local/ folder by default.
# export environment variables:
export LD_LIBRARY_PATH=/usr/local/lib
export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig
~/.bashrc
# change to pocketsphinx folder and perform the same steps
./configure
make
[sudo] make install

# Test
# To test installation, run 
pocketsphinx_continuous -inmic yes
# and check that it recognizes words you are saying to the microphone.
```

######  others

```bash
# Install pyaudio
# Ref: https://pyspotify.mopidy.com/en/latest/api/sink/
# Ref: https://stackoverflow.com/questions/35708238/installing-pyaudio-with-pip-in-a-virtualenv
sudo apt-get install portaudio19-dev
pip install --allow-unverified=pyaudio pyaudio
```

###### pocketsphinx-python

```bash
# Ref: https://pypi.python.org/pypi/pocketsphinx
# Make sure we have up-to-date versions of pip, setuptools and wheel:
$ pip install --upgrade pip setuptools wheel
# Ubuntu requirements:
$ sudo apt-get install -qq python python-dev python-pip build-essential swig git libpulse-dev
$ pip install --upgrade pocketsphinx
```

###### LiveSpeech Test

```python
from pocketsphinx import LiveSpeech
for phrase in LiveSpeech(): print(phrase)
```

```markdown
http://blog.justsophie.com/python-speech-to-text-with-pocketsphinx/
```

[demo code](script src="https://gist.github.com/srli/72c7938230537b4f8a4c.js"></script)

![](https://slack-files.com/T660HJN93-F660Z57MH-9e398b1d2e)

