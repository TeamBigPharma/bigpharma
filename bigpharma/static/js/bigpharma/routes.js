var app = angular.module('opal');
app.config(
    ['$routeProvider',
     function($routeProvider){
	     $routeProvider.when('/',  {redirectTo: '/formulation'})
             .when('/formulation', {
                 controller: 'CDRCtrl',
                 resolve: {
                     profile: function(UserProfile){ return UserProfile },
                     patients: function(Patients){ return Patients },
                     formulations: function(Formulations){ return Formulations }
                 },
                 templateUrl: '/templates/bigpharma/index.html'
             })
         
     }]);

