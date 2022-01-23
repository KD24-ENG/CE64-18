<script>
    import { Line } from 'vue-chartjs'

    export default {
        extends: Line,
        data () {
        return {
        chartData: {
            labels: ["07.00", "08.00", "09.00", "10.00", "11.00", "12.00", "13.00", "14.00", "15.00", "16.00", "17.00", "18.00", "19.00", "20.00", "21.00", "22.00"],
            datasets: [
                {
                label: 'สถิติจราจรจลอดวัน',
                data: [4000, 6000, 3500, 2500, 2000, 3000,	2000, 1000, 2300, 6000, 8000, 10000, 8000, 7000, 6500, 3000],
                fill: false,
                borderColor: '#2554FF',
                backgroundColor: '#2554FF',
                borderWidth: 1
                }
            ]
            },
            options: {
            scales: {
                yAxes: [{
                ticks: {
                    beginAtZero: true
                },
                gridLines: {
                    display: true
                }
                }],
                xAxes: [ {
                gridLines: {
                    display: false
                }
                }]
            },
            legend: {
                display: true
            },
            responsive: true,
            maintainAspectRatio: false
            }
        }
        },
        mounted () {
        this.renderChart(this.chartData, this.options)
        }
    }
    </script>