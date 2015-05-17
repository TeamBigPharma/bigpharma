angular.module('opal.services')
    .factory('Patients', function($q, $http, $window){
        var deferred = $q.defer();

        $http.get('/api/v0.1/patient/').then(function(response){
            deferred.resolve(response.data);
        });
        
        return deferred.promise;
    });
