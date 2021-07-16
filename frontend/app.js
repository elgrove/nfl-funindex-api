window.addEventListener('load', () => {

    const api = `http://127.0.0.1:8000/api/?season=2020&week=17`
    //const api = new Request('data.json')

    let table = document.querySelector('table')
    let header = []

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

    fetch(api)
        .then(response => {
            return response.json()
        })
        .then(data => {
            console.log(data.results)
            header = Object.keys(data.results[0])
            generateTable(table, data.results)
            generateTableHead(table, header)
        })
    

})
