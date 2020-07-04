//var myCat = {
//   "name": "Mewsalot",
//  "species": "cat",
//    "favFood": "tuna"
//}

// dane z atrybutu "name" obiektu "myCat"
//myCat.name

//var myFavColors = ["blue", "green", "purple"];

// dane z tablicy "myFavColors" o indeksie "1" (indeksowane od "0")
//myFavColors[1]



//var thePets = [
//    {
//    "name": "Mewsalot",
//    "species": "cat",
//    "favFood": "tuna"
//    },
//    {
//    "name": "Barky",
//    "species": "dog",
//    "favFood": "carrot"
//    }
//]

//console.log(thePets[1].name)

/*var pageCounter = 1;
var animalContainer = document.getElementById("animal-info")
var btn = document.getElementById("btn");

btn.addEventListener("click", function () {
    var ourRequest = new XMLHttpRequest();
    ourRequest.open('GET', 'https://learnwebcode.github.io/json-example/animals-' + pageCounter + '.json');
    ourRequest.onload = function () {
        var ourData = JSON.parse(ourRequest.responseText);
        renderHTML(ourData);
    };
    ourRequest.send();
    pageCounter++;
    if (pageCounter > 3) {
        btn.classList.add("hide-me");
    }
});

function renderHTML(data) {
    var htmlString = "";

    for (i = 0; i < data.length; i++) {
        htmlString += "<p>" + data[i].name + " is a " + data[i].species + "that likes to eat ";

        for (ii = 0; ii < data[i].foods.likes.length; ii++) {
            if (ii == 0) {
                htmlString += data[i].foods.likes[ii];
            } else {
                htmlString += " and " + data[i].foods.likes[ii];
            }
        }

        htmlString += ' and dislikes ';

        for (ii = 0; ii < data[i].foods.dislikes.length; ii++) {
            if (ii == 0) {
                htmlString += data[i].foods.dislikes[ii];
            } else {
                htmlString += " and " + data[i].foods.dislikes[ii];
            }
        }

        htmlString += '.</p>';
    }

    animalContainer.insertAdjacentHTML('beforeend', htmlString)
}
*/

$(function () {

    var $orders = $('#orders');

    $.ajax({
        type: 'GET',
        url: '/api/orders',
        success: function(orders) {
            $.each(orders, function (i, order) {
                $orders.append('<li>name: '+order.name+', drink: '+order.drink+'</li>');
            });
        },
        error: function () {
            alert('error loading orders');
        }
    });
});