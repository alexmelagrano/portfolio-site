/**
 * Created by alexmelagrano on 6/16/17.
 */

/**
 * On pageload, make API requests for Twitter and Spotify information to fill their HTML widgets.
 */
var main = function(){
    // Twitter


    // Spotify
    $.get('http://127.0.0.1:5000/api/get-tracks/', function(data, response){
        if (response == 200 || response == 'success'){
            console.log("Spotify response: " + response + "\nHere's the data:");
            console.log(data);

            var baseUrl = 'https://open.spotify.com/embed?uri=spotify:track:'

            for (var i = 0; i < 3; i++){
                var trackUrl = baseUrl + data['track' + (i + 1)];
                console.log(trackUrl);
                var iframeID = "#track-" + (i + 1);
                console.log(iframeID);
                var iframe = $(iframeID);
                iframe.attr('src', trackUrl);
                console.log(iframe.attr('src'));
            }
        } else {
            console.log("Couldn't retrieve Spotify track data: response " + response);
        }
    })
};


$(document).ready(main);