function readFirstOnly() {
    var data = getCSV(); //最初に実行される
    console.log(data)
    var ctx = document.getElementById('myLineChart').getContext('2d');
    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'line',
    
        // The data for our dataset
        data: {
            labels: [
                "2020/04/01",
                "2020/04/02",
                "2020/04/03",
                "2020/04/04",
                "2020/04/05",
                "2020/04/06",
                "2020/04/07",
                "2020/04/08",
                "2020/04/09",
                "2020/04/10",
                "2020/04/11",
                "2020/04/12",
                "2020/04/13",
                ],
            datasets: [
                {
                    label: 'Sleep(hour)',
                    borderColor: 'rgb(99,132,255)',
                    data: [
                        7.5,
                        8.5,
                        8.5,
                        7.5,
                        8.5,
                        7,
                        5.5,
                        7,
                        7,
                        8,
                        7,
                        8.5,
                        7.5,
                    ]
                },
                {
                    label: 'Tea or Coffee(ml)',
                    borderColor: 'rgb(255,99,0)',
                    data: [
                        0,
                        0,
                        3.00,
                        6.00,
                        6.50,
                        3.00,
                        10.00,
                        5.50,
                        2.50,
                        7.00,
                        6.00,
                        3.00,
                        5.20,
                        ,
                        ,
                    ]
                },
            ]
        },
    
        // Configuration options go here
        options: {}
    });
}
