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

            // Yes, this looks gross. But it's faster than building a jQuery element, so suck it.
            $('.twitter-link').append('<div class="twitter-error">Couldn\'t retrieve twitter data, but don\'t worry -<br/>I\'m probably doing something cool.<br/><br/>Like croquet. Or going HAM at an estate sale.</div>')
        }
    })

    // Spotify

};


$(document).ready(main);