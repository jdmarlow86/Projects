var app = require('app');

var BrowserWindow = require('browser-window');



var mainWindow = null;



app.on('window-all-closed', function() {

 if (process.platform != 'darwin')

 app.quit();

});



app.on('ready', function() { 

 mainWindow = new BrowserWindow({width: 800, height: 600}); 

 mainWindow.loadUrl('C:\Users\J&E\Desktop\My_App\app' + '/index.html'); 

 mainWindow.on('closed', function() {

 mainWindow = null;

 }); 

});