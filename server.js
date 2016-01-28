var jsdom = require('jsdom');
var ziprip = require('ziprip');
var _ = require('underscore');
var zerorpc = require('zerorpc');


function extractAddresses (sanitizedHtml, done) {

  try {
    jsdom.env({html: sanitizedHtml, done: onHtmlConverted});
  } catch (e) {
    var msg = "jsdom error parsing html during address extraction";
    console.error(msg);
    console.trace(e);
    done(msg);
  }

  function onHtmlConverted (err, window) {
    if (!err) {
      var addressObjects = ziprip.extract(window.document);
      var addresses;
      addresses = addressObjects.map(formatForGeocode);
      addresses = addresses.map(cleanAddressString);
      addresses = addresses.filter(address => address.length > 0 && address.length < 128);
      console.error(addresses);
      done(null, _.uniq(addresses));
    } else {
      var msg = "Could not convert string to DOM with jsdom";
      console.error(msg);
      console.trace(err);
      return done(msg);
    }
  }
    
}

function formatForGeocode (addressObject) {
  return addressObject.formatForGeocode();
}

function cleanAddressString (str) {
  str = str.replace(/\\n/g, '');
  str = str.replace(/\\t/g, '');
  str = str.replace(/\\r/g, '');
  str = str.replace(/\s+/g, ' ');
  str = str.replace(/(, )+/g, ', ');
  str = str.replace(/^[ ,]+/g, '');
  str = str.trim();
  return str;
}

var server = new zerorpc.Server({
  extract: function(html, reply) {
    extractAddresses(html, function(err, result) {
      if (!err) {
        reply(null, result);
      } else {
        reply(err);
      }
    });
  }
});

server.bind("tcp://127.0.0.1:4242");
