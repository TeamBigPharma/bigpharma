angular.module('opal.controllers').controller(
    'CDRCtrl', function($scope, $rootScope, $http,
                        profile,
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
            $http.post('/api/supply_to_ward/', $scope.ward).then(
                function(){
                    $scope.set_state('Initial');
                    growl.info('Supplied to ward');
                    $scope.ward = {};
                }, 
                function(data){
                    console.log(data);
                    alert(data);
                });
        }
        
        $scope.back_to_initial = function(){
            $scope.initial_state()
        }
    }
);
