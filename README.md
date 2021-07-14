# BookAudio audio book scraper
So I found this neat website: https://bookaudio.online/
They have tons of wonderful audiobooks to listen to, but no good way to download the files. I decided to solve that with this project.

Software assumed you have installed:
+ Docker
+ Python 3.7+
+ virtualenv


Should work about the same in any OS, but this is specifically for Linux and OSX.

Instructions from your terminal:

1. Clone the codebase locally:
<pre><code>git clone https://github.com/treybrooks/BookAudioDownloader.git
</code></pre>

2. Get your virtual environment setup and activated:
<pre><code>virtualenv --python=/usr/bin/python3.9 env
</code></pre>
<pre><code>source ./env/bin/activate
</code></pre>

3. Install the prerequisite packages:
<pre><code>pip install -r requirements.txt
</code></pre>

4. In a SEPARATE terminal Download and Run the Splash Browser Emulator:
<pre><code>sudo docker pull scrapinghub/splash
</code></pre>
<pre><code>sudo docker run -it -p 8050:8050 --rm scrapinghub/splash
</code></pre>

5. DOWNLOAD BOOKS:
<pre><code>scrapy crawl bookspider -a bookid="651-dune"
</code></pre>


For future use just make sure that browser emulator is running, reactivate the virtual env, then download whatever book they have to offer.