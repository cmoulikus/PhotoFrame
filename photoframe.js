var bleno = require('bleno');
var fs = require('fs');
var sys = require('sys');
var child_process = require('child_process');
var Descriptor = bleno.Descriptor;
var descriptor = new Descriptor({
     uuid: '2901',
      value: 'test write' // static value, must be of type Buffer or string if set
});

var Characteristic = bleno.Characteristic;
var myrun;
var cmdstr;
var characteristic = new Characteristic({
    uuid:  '01010101010101010101010101010111',
    properties: ['write', 'writeWithoutResponse','notify'],
  //  value: 'ff', // optional static value, must be of type Buffer
    descriptors: [ descriptor ],
    onWriteRequest: function(data, offset, withoutResponse, callback) {
    console.log('************************');
	console.log('We got: ' + data); // THIS BIT HERE is where we get data
	var str = data.toString('utf8');
	if(str=="PLAY"){
	    console.log('PLAY');
	}
	else if(str=="STOP"){
	    console.log('STOP');
	}
	else if(str=="FF"){
	    console.log('FF');
	}
	else if(str=="REWIND"){
	    console.log('REWIND');
	}
	else{
	    console.log('Unknown Command');
	}

//	fs.writeFile("command.txt",str); 
//	fs.close();
     
   callback(Characteristic.RESULT_SUCCESS);
    }
   });
var PrimaryService = bleno.PrimaryService;
var primaryService = new PrimaryService({
   //   uuid: 'fffffffffffffffffffffffffffffff0',
        uuid:  '01010101010101010101010101010101',
    characteristics: [ characteristic ]
   
  });
var services = [ primaryService ];
bleno.on('advertisingStart', function(error){
		        console.log('on -> advertisingStart: ' + (error ? 'error ' + error : 'success'));
		if(!error){
			   
			  bleno.setServices( services );
			  }
 });
bleno.on('stateChange', function(state) {
	 console.log('BLE stateChanged to: ' + state);
	 if (state === 'poweredOn') {
//	    bleno.startAdvertising('photopi',['fffffffffffffffffffffffffffffff0']);
	    bleno.startAdvertising('photopi',['01010101010101010101010101010101']);
	    } else {
	      bleno.stopAdvertising();
            }
});
