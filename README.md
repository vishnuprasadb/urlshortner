## Getting Started

1. Make sure you have `python` module, if not download it from [here](https://www.python.org/downloads/).
2. Make sure you have `pip` module, if not download it from [here](https://pypi.org/project/pip/)
3. Create a virtual environment using this command `python -m venv <virtualEnvNameOfYourChoice>`.
4. Activate the virtual environment using `source <virtualEnvNameOfYourChoice>/bin/activate`
5. Clone this github directory into the virtual environment created above. 
6. Go to the root directory in the repo `urlshortner` and run this command `pip install -r requirements.txt` to install all the dependencies.
7. Then run `./build.sh' from the same directory.

You are ready to go now.

## Problem Statement

Create a URL shortener library (e.g., bitly). Given a long URL, your program should return a shortened URL. Ensure the following: 

1. for a long URL X, your program should always return the shortened URL x 
2. for a short URL x that your program has generated, it should be able to return the original long URL X
3. the short URLs your program returns, must not follow any pattern; successive calls to your program should return very different short URLs. For example,
GOOD: a1x2l3, zAb3gr, ...
BAD: a1x213, a1x214, ... 
4. for two different long URLs X and Y, your program should (ideally) always return two different shortened URLs x and y 
5. your program must be able to accept long URLs provided both through console as well as from a file of newline separated long URLs 
6. the program should work for input files with up to 100,000 URLs without crashing 
7. we should be able to import your code as a module and use it, for example: 
import shortener

short_url = shortener.shorten(long_url); 

long_url = shortener.original(short_url)

## How to create a short url using this project?
1. Copy `createShortUrl.py` from scripts folder to root directory using this command `cp scripts/createShortUrl.py .`
2. Run the script `createShortUrl.py` with an argument which is the "Long url to be shortened". For Example:
	`python createShortUrl.py "www.google.com"`
3. To create short urls from a file copy 'bulkUrlShortner.py' from scripts folder like this `cp scripts/bulkUrlShortner.py .`.
4. Run the script `bulkUrlShortner.py` with an argument which is a txt file with newline separated long URLs. For Example:
	`python bulkUrlShortner.py test_input.txt`

## How to fetch a long url from a short url in this project?
1. Copy `getLongUrl.py` from scripts folder to root directory using this command `cp scripts/getLongUrl.py .`
2. Run the script `getLongUrl.py` with an argument which is the "short url". For Example:
	`python createShortUrl.py "https://xyz.com/aABadf"`

## Bulk Shortening results

Used the file `test_bulk_file.txt` to upload `100000` records and the output is found in `test_bulk_file-output.txt`.
All the url are shortned without crashing. Updating the database as well to check the results.
Also I have cross verified the entries randomly and its perfectly fine.