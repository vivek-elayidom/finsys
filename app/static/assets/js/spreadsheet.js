var headers = ["ID", "Module", "Feature", "Web", "Mobile", "Integration", "Consulting", "FrontEnd"];


function createCell(rowNum, columnNum, widthOptions) {
    var columnWidthOptions = widthOptions;
    console.log("ColumnNum is ", columnNum);
    var cell = document.createElement('input');
    cell.style.backgroundColor = '#d1e0e0';
    cell.style.border = "1px";
    cell.style.height = "30px";
    cell.style.borderColor = "#f0f5f5";
    cell.style.width = columnWidthOptions[columnNum].toString() + "px";
    cell.style.cursor = "pointer";
    if (rowNum == 0) {
        cell.value = headers[columnNum];
        cell.setAttribute("readOnly", "true");
        //console.log("will configure headers here", cell.value);
    }
    return cell;

}

function createSingleCell(index, columnWidthOptions, currentRowsNum) {
    //console.log("Adding a cell at index -", index, "number of presentcolumns is =", currentRowsNum);
    var cell = document.createElement('input');
    cell.style.backgroundColor = '#d1e0e0';
    cell.style.border = "1px";
    cell.style.height = "30px";
    cell.style.borderColor = "#f0f5f5";
    cell.style.width = columnWidthOptions[index].toString() + "px";
    cell.style.cursor = "pointer";
    cell.classList.add('cell');
    if (index == 0) {
        console.log("logging ID");
        cell.setAttribute("value", currentRowsNum - 1);
        cell.setAttribute("readOnly", "true");

        //console.log(cell.value);
    }
    return cell;
}

function addRow(numColumns, columnWidthOptions) {
    var table = document.getElementById('table1');
    var virtualRow = table.insertRow(-1);
    var currentRowsNum = table.rows.length;
    //var k = virtualRow.insertCell(0);
    //k.innerHTML = createSingleCell(0, columnWidthOptions).outerHTML;
    for (i = 0; i < columnWidthOptions.length; i++) {
        var k = virtualRow.insertCell(i);
        k.innerHTML = createSingleCell(i, columnWidthOptions, currentRowsNum).outerHTML;
        k.classList.add('cell');
        console.log(k);
    }
    //console.log(createSingleCell(0, columnWidthOptions), "is the return from Single Cell Create");
    //var l = virtualRow.insertCell(1);
    //l.innerHTML = "HI there";

    console.log(virtualRow, "is the virtualRow");
}


function createTable(tableName, numRows, numColumns, columnWidthOptions) {

    var table = document.createElement("table");
    for (i = 0; i < numRows - 1; i++) {
        var tr = document.createElement('tr');
        for (j = 0; j < numColumns; j++) {
            var td = document.createElement('td');
            var cellContent = createCell(i, j, columnWidthOptions);
            td.style.padding = "0px";
            td.style.border = "1px";

            td.appendChild(cellContent);
            tr.appendChild(td);
        }
        table.appendChild(tr);
    }
    table.setAttribute("name", tableName);
    table.setAttribute("id", 'table1');
    table.style.marginLeft = "20%";
    return table;
}


var TableObject = {

    headers = ["ID", "Column1", "Column2", "Column3", "Column4", "Column5"],
    row1 = [1, "How the fuck is this boss", "Column2 is nonsense", "Column3", "Column4 is nonsense", "Column5"],
    row2 = [1, "How the fuck is this boss", "Column2 is nonsense", "Column3", "Column4 is nonsense", "Column5"]
}