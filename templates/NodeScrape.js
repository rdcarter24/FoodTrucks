
var request = require('request');
var cheerio = require('cheerio');

var url = "http://www.foodtrucksmap.com/sf/"
request(url, function(err, resp, body) {
    if (err)
        throw err;
    var $ = cheerio.load(body);

    var truck_dict = {};
    var truck_name;
    function truck(TruckName, TruckLocation, schedule){
            this.TruckName= TruckName;
            this.TruckLocation = TruckLocation;
            this.schedule = schedule;

        }

    $('#open_trucks_list .truck_info').each(function(){
        $(this).find('h2').each(function(){
            truck_name = $(this).text();
        });
        var info_list = []
        $(this).find('p').each(function(){

            info_list.push($(this).text());
        });

    truck_dict[truck_name]=info_list

    });
for (key in truck_dict){
    console.log(key)
    console.log(truck_dict[key][1])
}




});