var express = require('express');
var mustache = require('mustache');
var app = express();
var path = __dirname+'/static/';

app.use(express.static(__dirname + '/styles'));

//----------------------------------------------------------------------------------------------------------------------
//Routen
//----------------------------------------------------------------------------------------------------------------------
app.get('/', function(req, res){
    //console.log('geht');
    res.sendFile(path+'index.html');
});
app.get('/:pagename(\\w+)', show);

//----------------------------------------------------------------------------------------------------------------------
//Funktionen
//----------------------------------------------------------------------------------------------------------------------
function show(req, res, next){
    var page = req.params['pagename'];
    res.sendFile(path+'/'+page+'.html');
}


//----------------------------------------------------------------------------------------------------------------------
//Server start
//----------------------------------------------------------------------------------------------------------------------
app.listen(8080, function(){
    console.log('server is running on localhost: '+'8080');
});