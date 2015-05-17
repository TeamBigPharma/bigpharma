angular.module('opal.controllers')
    .controller('CDRAddPatientCtrl', function(
        $scope, $modalInstance, $rootScope, $http,
        Episode
    ){

        $scope.editing = {
            location: {},
            demographics: {}
        };
        
        $scope.save = function(){
	    $http.post('episode/', $scope.editing).success(function(episode) {
		episode = new Episode(episode);
		$modalInstance.close($scope.editing.demographics.name);
	    });            
        };
        
	$scope.cancel = function() {
	    $modalInstance.close(null);
	};

        
    })
