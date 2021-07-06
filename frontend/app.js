window.addEventListener('load', () => {

    // const api = `http://127.0.0.1:5000/api/?season=2020&week=17`
    const myRequest = new Request('data.json')

    let table_data
    let table = document.querySelector('table')


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

    fetch(myRequest)
        .then(response => response.json())
        .then(data => {
            header = Object.keys(data[0])

            generateTable(table, data)
            generateTableHead(table, header)
        })
    



})
