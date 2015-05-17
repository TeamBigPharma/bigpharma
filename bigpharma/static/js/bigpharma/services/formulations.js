angular.module('opal.services')
    .factory('Formulations', function($q, $http, $window){
        var deferred = $q.defer();

        $http.get('/api/drug_formulation/').then(function(response){
            deferred.resolve(response.data);
        });
        
        return deferred.promise;
    });
