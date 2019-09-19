from blueRest import BlueData


def connect(config):
    restClient = BlueData(config)
    restClient.connect()
    tenants = restClient.getTenants()
    sessionid = restClient.getSessionId()
    return { 'sessionid': sessionid, 'tenants': tenants, 'templates': [] }
  
    
def templates(config):
    tenant = config["selectedTenant"]
    restClient = BlueData(config)
    restClient.connect( tenant['label']['name'] )
    templates = restClient.getTemplates()
    return { "templates": templates }


actions = {
    "connect": connect,
    "templates": templates
}


def do(payload, config, plugin_config, inputs):  
    return actions[payload["method"]](config)
