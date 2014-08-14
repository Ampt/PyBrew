/**
 * Created by Matthew on 8/13/2014.
 */

app.Brew = Backbone.Model.extend({

    // Default attributes ensure that each todo created has `title` and `completed` keys.
    defaults: {
        name: '',
        color: ''
    },

    // Toggle the `completed` state of this todo item.
    toggle: function() {
        this.save({
            completed: !this.get('completed')
        });
    }

});