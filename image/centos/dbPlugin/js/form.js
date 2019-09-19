var app = angular.module('myplugin.module', []);

app.controller('MyCustomFormController', function($scope) {
    
    $scope.config.hostname = "35.177.158.117"
    $scope.config.username = "admin"
    $scope.config.password = "admin123"
    $scope.config.selectedTenant = null
    $scope.config.selectedTemplate = null
    $scope.config.clustername = ""
    $scope.config.clusterdescription = ""
    
    $scope.config.sessionid = ""
    
    $scope.connect = function() {
        if ( $scope.config.hostname ) {
            $scope.callPythonDo({ "method": "connect" }).then(function(data) {
                $scope.tenants = data.tenants
                $scope.config.sessionid = data.sessionid
                $scope.config.selectedTenant = $scope.tenants[0]
                $scope.tenantChange()
            }, function(data) {
                $scope.tenants = [];
                $scope.templates = [] 
            });
        } else {
            $scope.tenants = [] 
            $scope.templates = [] 
        }
    };
    
    
    var templateChange = function() {
        if ( $scope.config.selectedTemplate ) {
            var currentTemplate = $scope.config.selectedTemplate['_embedded']['label']
            $scope.config.clustername = currentTemplate['name']
            $scope.config.clusterdescription = currentTemplate['description']
        } else {
            $scope.config.clustername = ""
            $scope.config.clusterdescription = ""
        }
    }
  

    var tenantChange = function() {
        if ( $scope.config.selectedTenant ) {
            $scope.callPythonDo({ "method": "templates" }).then(function(data) {
                $scope.templates = data.templates;
                $scope.config.selectedTemplate = $scope.templates[0]
                $scope.templateChange()
            }, function(data) {
                $scope.templates = [];
            });
        } else {
            $scope.templates = [] 
            $scope.config.selectedTemplate = null
        }
    };
    
    
    $scope.$watch('config.selectedTenant', tenantChange);
    $scope.$watch('config.selectedTemplate', templateChange);
});


 
  