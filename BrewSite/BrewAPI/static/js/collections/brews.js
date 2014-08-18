var app = app || {};

var BrewList = Backbone.Collection.extend({

    // Reference to this collection's model.
    model: app.Brew,


});

// Create our global collection of **Todos**.
app.Brews = new BrewList();