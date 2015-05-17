angular.module('opal.controllers').controller(
    'CDRCtrl', function($scope, $rootScope, profile,
                        growl,
                        formulations){
        
        $scope.state = 'Initial';
        $scope.profile = profile;
        $scope.formulations = formulations;
        $scope.drug_list = _.map(formulations, function(f){ return f.drug });

        $scope.booking = {};
        $scope.patient = {};
        
        $scope.set_state = function(what){ $scope.state = what };

        $scope.save_booking = function(){
            $scope.set_state('Initial');
            growl.info('Booked in delivery!')
            $scope.booking = {}
        };

        $scope.save_patient = function(){
            $scope.set_state('Initial');
            growl.info('Dispensed to Patient')
            $scope.patient = {};
        }
        
    }
);
