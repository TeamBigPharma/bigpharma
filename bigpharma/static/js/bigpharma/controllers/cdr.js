function onlyUnique(value, index, self) { 
    return self.indexOf(value) === index;
}
angular.module('opal.controllers').controller(
    'CDRCtrl', function($scope, $rootScope, $http, $modal,
                        profile,
                        growl,
                        formulations, patients){
        
        $scope.profile = profile;
        $scope.formulations = formulations;
        $scope.patients = patients;
        $scope.patient_name_list = _.map(patients, function(p){
            return p.demographics[0].name
        }).filter(onlyUnique);
        console.log($scope.patient_name_list);
        $scope._drug_names_to_id = {}
        $scope.drug_list = _.map(formulations, function(f){
            var name = f.drug + ' ' + f.amount + ' ' + f.units;
            $scope._drug_names_to_id[name] = f.id
            return name
        });

        console.log($scope.formulations)
        console.log($scope.drug_list)
        
        $scope.initial_state = function(){
            $scope.state = 'Initial';
            $scope.booking = {datetime: new Date()};
            $scope.patient = {datetime: new Date()};
            $scope.ward = { datetime: new Date() };
        };
        $scope.initial_state();
        
        $scope.set_state = function(what){ $scope.state = what };

        $scope.save_booking = function(){
            $scope.set_state('Initial');
            growl.info('Booked in delivery!')
            $scope.booking = {}
        };

        $scope.save_patient = function(){
            var data = {
                amount: $scope.patient.quantity,
                datetime: moment($scope.patient.datetime).format(),
                formulation: $scope._drug_names_to_id[$scope.ward.product],
                patient: $scope.patient.patient_name,
                supplied_individual: $scope.patient.collector || "Patient",
                collected_by_patient: $scope.patient.collected_by_patient
            };
            $http.post('/api/supplied_from_pharmacist/', data).then(
                function(){
                    $scope.set_state('Initial');
                    growl.info('Supplied to Patient')
                    $scope.patient = {};
                },
                function(data){
                    console.log(data);
                    alert(data);
                }
            )
        }

        $scope.save_ward = function(){
            var data = {
                amount: $scope.ward.quantity,
                supplied_individual: $scope.ward.collector,
                ward: $scope.ward.ward_name,
                datetime: moment($scope.ward.datetime).format(),
                formulation: $scope._drug_names_to_id[$scope.patient.product]
            }
            $http.post('/api/supplied_from_pharmacist/', data).then(
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

        $scope.add_patient = function(){
            $modal.open({
                templateUrl: '/templates/modals/add_patient.html',
                controller: 'CDRAddPatientCtrl',
                resolve: {
                }
            }).result.then(function(name){
                if(name =='cancel'){
                    return
                }else{
                    $scope.patient_name_list.push(name)
                    $scope.patient.patient_name = name;
                }
            });
        }
    }
);
