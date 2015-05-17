var app = angular.module('opal');
app.config(
    ['$routeProvider',
     function($routeProvider){
	     $routeProvider.when('/',  {redirectTo: '/formulation'})
             .when('/formulation', {
                 controller: 'FormulationCtrl',
                 resolve: {
                     profile: function(UserProfile){ return UserProfile }
                 },
                 templateUrl: '/templates/bigpharma/index.html'
             })
         
     }]);

