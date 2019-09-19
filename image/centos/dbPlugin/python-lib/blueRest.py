import json
import requests

class BlueData(object):
   
    def _sessionExists(self):
        return True if self.headers['X-BDS-SESSION'] != null else False;
    
    def getSessionId(self):
        return self.headers['X-BDS-SESSION']
        
        
    def _invoke(self, path, payload={}, verb="GET"):
        count = 0
        while count <= self.retries:
             try:
                 response = requests.request( verb, self.base + path, headers=self.headers, data=json.dumps(payload), verify=False)
                 if response.ok:
                     return response
                 else:
                    response.raise_for_status()
             except IOError:
                 count += 1
                 time.sleep(5)
        return response


    def __init__(self, config, retries=10):
        self.config = config
        self.retries = retries
        self.base = "http://" + config['hostname'] + ":8080"
        self.user = { "name":  config['username'], "password": config['password'] }
        self.session = { "password": config['password'], "site_admin_view": True }
        self.headers =  { "Accept": "applicaiton/json", "Content-type": "application/json" }


    def connect(self,tenantName="Site Admin"):
        response = self._invoke( "/api/v2/session/", self.user, "POST")
        self.sessionid = response.headers['Location']
        self.headers['X-BDS-SESSION'] = self.sessionid 
        self.session["tenant_name"] = tenantName
        response = self._invoke( "/api/v2/session/", self.session, "POST")
        

    def getTenants(self):
        response = self._invoke("/api/v2/tenant/")
        if response.ok:
            data = json.loads(response.content)
            return data["_embedded"]["tenants"]
        else: 
            return []


    def getTemplates(self):
        response = self._invoke("/api/v2/template/")
        if response.ok:
            data = json.loads(response.content)
            return data["_embedded"]["templates"]
        else: 
            return []
            

    def createCluster(self, clusterspec):
        response = self._invoke("/api/v2/cluster/", clusterspec, "POST")
        if response.ok:
            return response.headers['Location']
        else: 
            return {}
        
        
    def getCluster(self,clusterid):
        response = self._invoke(clusterid)
        if response.ok:
            return json.loads(response.content)
        else:
            return {} 
        
    def getNodes(self,clusterid):
        response = self._invoke(clusterid + "/node")
        if response.ok:
            return json.loads(response.content)['_embedded']['nodes']
        else:
            return {} 
        
    def getServices(self, nodeid):
        response = self._invoke(nodeid + "?services")
        if response.ok:
            return json.loads(response.content)['services']
        else:
            return {} 
        

  