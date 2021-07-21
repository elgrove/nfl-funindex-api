let current_season
let current_week
let raw_api = `http://127.0.0.1:8000/r`
let query_api
let week_selection
let season_selection

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

window.addEventListener('load', () => {

    fetch(raw_api)
        .then(response => {
            return response.json()
        })
        .then(raw_data => {
            current_season = raw_data.results[0].season
            current_week = raw_data.results[0].week
            document.getElementById('season_select').value = current_season
            document.getElementById('week_select').value = current_week
            query_api = `http://127.0.0.1:8000/q/?season=${current_season}&week=${current_week}`
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


document.getElementById('week_select').addEventListener('change', (event) => {
    week_selection = event.target.value
    query_api = `http://127.0.0.1:8000/q/?season=${current_season}&week=${week_selection}`
    header.innerHTML = ''
    table.innerHTML = ''
    fetch(query_api)
    .then(response => {
        return response.json()
    })
    .then(query_data => {;
        console.log(query_data)
        query_week = week_selection
        current_season = document.getElementById('season_select').value
        generateTable(table, query_data.results)
        generateTableHead(table, header)        
        document.getElementById('current_week_header').innerHTML = `Week ${query_week}, ${current_season} Season`
    })
})

document.getElementById('season_select').addEventListener('change', (event) => {
    season_selection = event.target.value
    current_week = document.getElementById('week_select').value
    query_api = `http://127.0.0.1:8000/q/?season=${season_selection}&week=${current_week}`
    header.innerHTML = ''
    table.innerHTML = ''
    fetch(query_api)
    .then(response => {
        return response.json()
    })
    .then(query_data => {;
        query_season = season_selection
        current_week = document.getElementById('week_select').value
        generateTable(table, query_data.results)
        generateTableHead(table, header)        
        document.getElementById('current_week_header').innerHTML = `Week ${current_week}, ${query_season} Season`
    })
})