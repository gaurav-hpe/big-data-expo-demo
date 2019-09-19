from blueRest import BlueData
from dataiku.runnables import Runnable


class MyRunnable(Runnable):
    
    def __init__(self, project_key, config, plugin_config):
        self.config = config
        self.project_key = project_key
        self.plugin_config = plugin_config     
       
        
    def get_progress_target(self):
        return None

    def run(self, progress_callback):
        tenant = self.config["selectedTenant"]
        
        restClient = BlueData(self.config)
        restClient.connect(tenant['label']['name'])
        
        clusterSpec = self.config['selectedTemplate']['_embedded']['clusterspec']
        clusterSpec['label'] = { "name": self.config['clustername'], "description": self.config['clusterdescription'] }

        clusterId = restClient.createCluster(clusterSpec)
        nodes = restClient.getNodes(clusterId)
        
        result = []
        for node in nodes:
            result.append( restClient.getServices( node['_links']['self']['href'] ))
       
        
        return '<div>The Cluster has been created sucessfully:</div><pre class="debug">%s</pre>' % result 