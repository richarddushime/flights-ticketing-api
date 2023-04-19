$(document).ready(function() {
    $('input[name="origin"]').autocomplete({
        source: function(request, response) {
            $.ajax({
                url: "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/",
                headers: {
                    "X-RapidAPI-Host": "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
                    "X-RapidAPI-Key": "e7811949dbmsh1bc1dad35f0d819p12c788jsn23611ad30e78"
                },
                dataType: "json",
                data: {
                    query: request.term
                },
                success: function(data) {
                    var results = $.map(data["Places"], function(item) {
                        return {
                            label: item["PlaceName"] + ", " + item["CountryName"],
                            value: item["PlaceId"]
                        };
                    });

                    response(results);
                }
            });
        },
        minLength: 3
    });

    $('input[name="destination"]').autocomplete({
        source: function(request, response) {
            $.ajax({
                url: "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/",
                headers: {
                    "X-RapidAPI-Host": "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
                    "X-RapidAPI-Key": "e7811949dbmsh1bc1dad35f0d819p12c788jsn23611ad30e78"
                },
                dataType: "json",
                data: {
                    query: request.term
                },
                success: function(data) {
                    var results = $.map(data["Places"], function(item) {
                        return {
                            label: item["PlaceName"] + ", " + item["CountryName"],
                            value: item["PlaceId"]
                        };
                    });

                    response(results);
                }
            });
        },
        minLength: 3
    });
});
