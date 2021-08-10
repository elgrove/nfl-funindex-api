window.addEventListener('load', () => {

    let current_season
    let current_week
    let raw_api = `http://45.33.89.202:8000/r`
    let query_api
    //const api = new Request('data.json')


    let table = document.querySelector('table')
    let header = [
        'Date',
        'Time',
        'Away Team',
        'Home Team',
        'Fun Index'
    ]

    function generateTableHead(table, data) {
        let thead = table.createTHead()
        let row = thead.insertRow()
        for (let element of data) {
            let th = document.createElement('th')
            let text = document.createTextNode(element)
            th.appendChild(text)
            row.appendChild(th)
        }
    }
    
    function generateTable(table, data) {
        for (let element of data) {
            let row = table.insertRow()
            for (key in element) {
                let cell = row.insertCell()
                let text = document.createTextNode(element[key])
                cell.appendChild(text)
            }
        }
    }


    fetch(raw_api)
        .then(response => {
            return response.json()
        })
        .then(raw_data => {
            current_season = raw_data.results[0].season
            current_week = raw_data.results[0].week
            query_api = `http://45.33.89.202:8000/q/?season=${current_season}&week=${current_week}`
        fetch(query_api)
        .then(response => {
            return response.json()
        })
        .then(query_data => {
            generateTable(table, query_data.results)
            generateTableHead(table, header)
            document.getElementById('current_week_header').innerHTML = `Week ${current_week}, ${current_season} Season`
        })


        })
})


