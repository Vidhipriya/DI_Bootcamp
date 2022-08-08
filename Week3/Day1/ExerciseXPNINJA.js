let table = document.createElement('table');
let thead = document.createElement('thead');
let tbody = document.createElement('tbody');

table.appendChild(thead);
table.appendChild(tbody);

document.getElementById('body').appendChild(table);

let row_1 = document.createElement('tr');
let heading_1 = document.createElement('th');
heading_1.innerHTML = "Monday";
let heading_2 = document.createElement('th');
heading_2.innerHTML = "Tuesday";
let heading_3 = document.createElement('th');
heading_3.innerHTML = "Wednesday";
let heading_4 = document.createElement('th');
heading_4.innerHTML = "Thursday";
let heading_5 = document.createElement('th');
heading_5.innerHTML = "Friday";
let heading_6 = document.createElement('th');
heading_6.innerHTML = "Saturday";
let heading_7 = document.createElement('th');
heading_7.innerHTML = "Sunday";

row_1.appendChild(heading_1);
row_1.appendChild(heading_2);
row_1.appendChild(heading_3);
row_1.appendChild(heading_4);
row_1.appendChild(heading_5);
row_1.appendChild(heading_6);
row_1.appendChild(heading_7);
thead.appendChild(row_1);


for (var a=0; a < 7; a++) {
document.write("<tr>");
for(var b=0; b<7; b++) {
document.write("<td>"+"</td>");
}

document.write("</tr>");
}

// let row_2_data_1 = document.createElement('td');
// row_2_data_1.innerHTML = "1";
// let row_2_data_2 = document.createElement('td');
// row_2_data_2.innerHTML = "2";
// let row_2_data_3 = document.createElement('td');
// row_2_data_3.innerHTML = "3";
// let row_2_data_4 = document.createElement('td');
// row_2_data_4.innerHTML = "4";
// let row_2_data_5 = document.createElement('td');
// row_2_data_5.innerHTML = "5";
// let row_2_data_6 = document.createElement('td');
// row_2_data_6.innerHTML = "6";
// let row_2_data_7 = document.createElement('td');
// row_2_data_7.innerHTML = "7";


// row_2.appendChild(row_2);
// row_2.appendChild(row_2_data_2);
// row_2.appendChild(row_2_data_3);
// row_2.appendChild(row_2_data_4);
// row_2.appendChild(row_2_data_5);
// row_2.appendChild(row_2_data_6);
// row_2.appendChild(row_2_data_7);

tbody.appendChild(a);

function createCalendar(year,month){



}