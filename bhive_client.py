import boto3
import json
import requests

class BhiveClient(object):

	def __init__(self, api_token):
		self.api_token = api_token
		self.ec2client = boto3.client('ec2')

	def run(self):
		self.post_instances_public_ip_address()
		
	def post_instances_public_ip_address(self):
		response = self.ec2client.describe_instances()
		text = []
		for resev in response.get('Reservations', []):
			for inst in resev.get('Instances', []):
				name = ''
				state = inst.get('State', {}).get('Name', '')
				for t in inst.get('Tags', []):
					if t['Key'] == 'Name':
						name = t['Value']
				text.append("*%s* [%s]:\t_%s_" % (name, state, inst.get('PublicIpAddress')))
		if text:
			return self.update_integration(integration_id='post_instances_public_ip_address', data={
				"title": "EC2 public IPs", "text":"\n".join(text), "tags": "aws,amazon,servers,server,list"})

	def create_integration(self, integration_id):
		self.call_api(
			method="POST", 
			path="%s/create" % self.api_token, 
			data={ 'integration_id': integration_id })

	def update_integration(self, integration_id, data):
		path = "%s/%s" % (self.api_token, integration_id)
		res = self.call_api(method="PUT", path=path, data=data)
		if res.get('message') == "Intergation wasn't found":
			self.create_integration(integration_id)
		res = self.call_api(method="PUT", path=path, data=data)
		return res

	def call_api(self, method, path, data):
		headers = {"Content-Type": "application/json", "Accept": "application/json"}
		url = 'https://www.beehive.ai/api/integrations/%s' % path
		data = json.dumps(data)
		if method == 'PUT':
			return requests.put(url, data=data, headers=headers).json()
		if method == 'POST':
			return requests.post(url, data=data, headers=headers).json()


