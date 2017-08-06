/**
 * Created by alexmelagrano on 6/16/17.
 */

/**
 * On pageload, make API requests for Twitter and Spotify information to fill their HTML widgets.
 */
var main = function(){
    // Twitter
    $.get('http://127.0.0.1:5000/api/get-tweet', function(data, response){
        if (response == 200 || response == 'success'){
            console.log("Twitter response: " + response);

            $('.twitter-link').append(data)
        } else {
            console.log("Couldn't retrieve Twitter info. \nResponse: " + response);
            $('.twitter-link').append('<div class="twitter-error">Couldn\'t retrieve twitter data, but don\'t worry - I\'m doing stuff.</div>')
        }
    })

    // Spotify

};


$(document).ready(main);