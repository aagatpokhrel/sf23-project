graph_elm = document.getElementById("graph")

let data_elem = document.getElementById("data")
let data_raw = data_elem.innerText

let data = JSON.parse(data_raw);

// data_elem.remove();


var barColors = ["red", "green", "blue", "orange", "brown"];

let category_elm = document.getElementById("chart_category").getContext("2d");
new Chart(category_elm,{
        type: 'bar',
        data: {
            labels: data.category.x_values,
            datasets:[{
                data:data.category.y_values,
                backgroundColor: barColors,
            }]
        },
        options: {
        title: {
            display: true,
            text: "Category",
        },
        legend: {
            display: false
         },
        },
    }
)
let mop_elm = document.getElementById("chart_mode_of_payment").getContext("2d");
new Chart(mop_elm,{
        type: 'bar',
        data: {
            labels: data.mode_of_payment.x_values,
            datasets:[{
                data:data.mode_of_payment.y_values,
                backgroundColor: barColors,
            }]
        },
        options: {
        title: {
            display: true,
            text: "Mode of Payment",
        },
        legend: {
            display: false
         },
        },
    }
)

let expenseType_elm = document.getElementById("chart_expenseType").getContext("2d");

new Chart(expenseType_elm, {
type: "doughnut",
data: {
    labels: data.expense_type.x_values,
    datasets: [
    {
        data:data.expense_type.y_values,
        backgroundColor: barColors,
    },
    ],
},
options: {
    title: {
    display: true,
    text: "Expense Type",
    },
},
});

var chart_date_elm = document.getElementById("chart_date").getContext("2d");

new Chart(chart_date_elm, {
type: "line",
data: {
    labels: data.date.x_values,
    datasets: [
    {
        label: "Amount Spent per day",
        backgroundColor: "rgba(153, 102, 255, 0.5)", //purple
        borderColor: "rgba(153, 102, 255, 1)",
        data: data.date.y_values,
    },
    ],
},
options: {
    title: {
    display: true,
    text: "Time Series plot of expense",
    },
},
});