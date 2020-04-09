# heinsenberg
Tool to make a port scan through the API of Shodan, Censys, Onyphe and Binardy Edge


# Instalation

You can download the latest version of heinsenberg by cloning the GitHub repository:

<pre>git clone https://github.com/n4xh4ck5/heinsenberg </pre>

Install the dependencies via pip:

  <pre> pip install -r requirements.txt </pre>
  
 # Usage
 
 python3 eisenberg.py -i <IP.txt> -a <API.json>
  
 You need update your own API KEYS in the parameter file api.json. In the repository there is a example.
 
<pre>
python3 heisenberg.py -h
usage: heisenberg.py [-h] [-e EXPORT] -i INPUT -a API

Tool to make a port scan through the API of Shodan, Censys, Onyphe and Binardy Edge

optional arguments:
  -h, --help            show this help message and exit
  -e EXPORT, --export EXPORT
                        File in xlsx format which contains the ports opened (y/n)
  -i INPUT, --input INPUT
                        Input in txt with the IP's which it wants to analyze
  -a API, --api API     Input in json with the API key of the services. Please, read the example file
</pre>
  
# Dependencies

Dependencies in python3:

<pre>
  requests
  xlsxwriter
</pre>
  
# Author

Ignacio Brihuega Rodríguez aka n4xh4ck5

Twitter: @n4xh4ck5

Web: fwhibbit.es

# Disclamer

The use of this tool is your responsability. I hereby disclaim any responsibility for actions taken with this tool.
