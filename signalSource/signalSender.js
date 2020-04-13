
var request = require('request');

setInterval(function send() {

  const path = ""; // path to send GPS info x, y, z


  let x = 0;
  let y = 0;
  let z = 0;

  console.log(x, y, z);

  let url = path + (x + '/') + (y + '/') + (z + '/');

  request(url, function (error, response, body) {
    console.log('error:', error); // Print the error if one occurred
    console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
    console.log('body:', body); // Print the HTML for the Google homepage.
  });
}, 20000);


