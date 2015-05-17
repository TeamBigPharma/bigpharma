angular.module('opal.controllers').controller(
    'FormulationCtrl', function($scope, $rootScope, profile){
        
        $scope.state = 'Initial';
        $scope.profile = profile;

        $scope.booking = {};
        
        $scope.set_state = function(what){ $scope.state = what };
    }
)
