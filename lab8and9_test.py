#import requests
#res = requests.get('curl -s -X GET 'Accept: application/json' 127.0.0.1:8080/')
#res.json()


cmd = '''curl -s -X GET 'Accept: application/json' 127.0.0.1:8080/'''
args = cmd.split()
process = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.comunicate()
