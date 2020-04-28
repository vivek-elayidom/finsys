var headers = ["ID", "Module", "Feature", "Web", "Mobile", "Integration", "Consulting", "FrontEnd"];


function createCell(rowNum, columnNum, widthOptions) {
    var columnWidthOptions = widthOptions;
    //console.log("ColumnNum is ", columnNum);
    var cell = document.createElement('input');
    cell.style.backgroundColor = '#d1e0e0';
    cell.style.border = "0px";
    cell.style.height = "30px";
    cell.style.borderColor = "#f0f5f5";
    cell.style.width = columnWidthOptions[columnNum].toString() + "px";
    cell.style.cursor = "pointer";
    cell.setAttribute("row", rowNum);
    cell.setAttribute("column", columnNum);
    cell.setAttribute("class", "cell");
    if (rowNum == 0) {
        cell.value = headers[columnNum];
        cell.style.fontSize = '12px';
        cell.setAttribute("readOnly", "true");
        cell.style.backgroundColor = '#ffffff';
        //console.log("will configure headers here", cell.value);
    }
    return cell;

}

function createSingleCell(index, columnWidthOptions, currentRowsNum, tableID) {
    //console.log("Adding a cell at index -", index, "number of presentcolumns is =", currentRowsNum);
    var cell = document.createElement('input');
    cell.style.backgroundColor = '#d1e0e0';
    cell.style.border = "0px";
    cell.style.height = "25px";
    cell.style.fontSize = '12px';
    cell.style.borderColor = "#f0f5f5";
    cell.style.width = columnWidthOptions[index].toString() + "px";
    cell.style.cursor = "pointer";
    cell.setAttribute("onclick", "onclickListen(this)");
    cell.setAttribute("onkeyup", "onkeyupListen(this)");
    cell.setAttribute("column", index);
    cell.setAttribute("row", currentRowsNum - 1);
    cell.setAttribute("class", "cell");
    cell.setAttribute("id", tableID + '-' + (currentRowsNum - 1).toString() + '-' + index.toString())
    if (index == 0) {
        //console.log("logging ID");
        cell.setAttribute("value", currentRowsNum - 1);
        cell.setAttribute("readOnly", "true");
        //console.log(cell.value);
    }
    return cell;
}

class CellObject {
    constructor(row, column, value, tableID) {
        this.row = row;
        this.column = column;
        this.value = value;
        this.tableID = tableID;
    }
    getRow() {
        return this.row;
    }
    getColumn() {
        return this.column;
    }
    getValue() {
        return this.value;
    }
    getTableID() {
        return this.tableID;
    }
}

class SectionObject {
    constructor(value, sectionID) {
        this.value = value;
        this.section = sectionID;
    }

    getValue() {
        return this.value;
    }
    getSectionID() {
        return this.section;
    }
}




function addRow(numColumns, columnWidthOptions, tableID) {
    var table = document.getElementById(tableID);
    console.log("Addrow in js called on element ", tableID)
    var virtualRow = table.insertRow(-1);
    var currentRowsNum = table.rows.length;
    //var k = virtualRow.insertCell(0);
    //k.innerHTML = createSingleCell(0, columnWidthOptions).outerHTML;
    for (i = 0; i < columnWidthOptions.length; i++) {
        var k = virtualRow.insertCell(i);
        k.innerHTML = createSingleCell(i, columnWidthOptions, currentRowsNum, tableID).outerHTML;

        //k.classList.add('cell');
        console.log(k);
    }
    //console.log(createSingleCell(0, columnWidthOptions), "is the return from Single Cell Create");
    //var l = virtualRow.insertCell(1);
    //l.innerHTML = "HI there";

    // /console.log(virtualRow, "is the virtualRow");
}




function createTable(tableName, numRows, numColumns, columnWidthOptions) {

    var table = document.createElement("table");
    var tablebody = document.createElement("tbody");
    for (i = 0; i < numRows - 1; i++) {
        var tr = document.createElement('tr');
        for (j = 0; j < numColumns; j++) {
            var td = document.createElement('td');
            var cellContent = createCell(i, j, columnWidthOptions);
            cellContent.setAttribute("id", tableName + '-' + i.toString() + '-' + j.toString())
            td.style.padding = "0px";
            td.style.border = "0px";

            td.appendChild(cellContent);
            tr.appendChild(td);
        }
        tablebody.appendChild(tr);
    }
    table.appendChild(tablebody);
    table.setAttribute("name", tableName);
    table.setAttribute("id", tableName);
    table.style.marginLeft = "0%";
    return table;
}

/*
var TableObject = {

    headers = ["ID", "Column1", "Column2", "Column3", "Column4", "Column5"],
    row1 = [1, "How the fuck is this boss", "Column2 is nonsense", "Column3", "Column4 is nonsense", "Column5"],
    row2 = [1, "How the fuck is this boss", "Column2 is nonsense", "Column3", "Column4 is nonsense", "Column5"]
}
*/

function getCurrentTables() {

    var tables = document.getElementsByTagName('table');
    console.log("Number of tables is", tables.length);

    var htmlString = "";

    for (i = 0; i < tables.length; i++) {
        // /console.log(tables[i].id, "-is one table");
        //var rows = tables[i].rows;
        var containerParent = tables[i].parentNode;
        var rowParent = containerParent.parentNode;
        //console.log(rowParent.outerHTML);
        htmlString = htmlString + rowParent.outerHTML;

    }

    // /console.log(htmlString);
    return htmlString;
}

/*

{
    "estimateID": 12334,
    "section_name": "New Section",
    "headers": ["ID","Module","Feature","Web","Mobile","Consulting","Integration","Testing"],
    "columnDims":[30,60,120,50,50,50,50,50],
    "rows":{
        1: ["123","Module1","Login",20,30,40,50,20,20],
        
    }
}

{
    "id":"232322233",
    "rowtype":"header",//orData
    "data":["ID","ABCD",1,34,34,24],
    "estimateID":123454545,
    "sectionID":2232232,
}



*/