angular.module('opal.controllers').controller(
    'CDRCtrl', function($scope, $rootScope, profile,
                        growl,
                        formulations){
        
        $scope.profile = profile;
        $scope.formulations = formulations;
        $scope.drug_list = _.map(formulations, function(f){ return f.drug + ' ' + f.amount + ' ' + f.units });

        console.log($scope.formulations)
        console.log($scope.drug_list)
        
        $scope.initial_state = function(){
            $scope.state = 'Initial';
            $scope.booking = {};
            $scope.patient = {};
            $scope.ward = {};
        };
        $scope.initial_state();
        
        $scope.set_state = function(what){ $scope.state = what };

        $scope.save_booking = function(){
            $scope.set_state('Initial');
            growl.info('Booked in delivery!')
            $scope.booking = {}
        };

        $scope.save_patient = function(){
            $scope.set_state('Initial');
            growl.info('Supplied to Patient')
            $scope.patient = {};
        }

        $scope.save_ward = function(){
            $scope.set_state('Initial');
            growl.info('Supplied to ward');
            $scope.ward = {};
        }
        
        $scope.back_to_initial = function(){
            $scope.initial_state()
        }
    }
);
