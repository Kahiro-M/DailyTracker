function readFirstOnly() {
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
                // "2020/04/14",
                // "2020/04/15",
                // "2020/04/16",
                // "2020/04/17",
                // "2020/04/18",
                // "2020/04/19",
                // "2020/04/20",
                // "2020/04/21",
                // "2020/04/22",
                // "2020/04/23",
                // "2020/04/24",
                // "2020/04/25",
                // "2020/04/26",
                // "2020/04/27",
                // "2020/04/28",
                // "2020/04/29",
                // "2020/04/30",
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
                    ],
                    pointRadius:8,
                    pointBorderWidth:4,
                },
                {
                    label: 'Tea/Coffee(100ml)',
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
                    ],
                    borderDash: [8, 2],
                    pointStyle: 'crossRot',
                    pointRadius:8,
                    pointBorderWidth:4,
                },
            ]
        },
    
        // Configuration options go here
        options: {}
    });
}
