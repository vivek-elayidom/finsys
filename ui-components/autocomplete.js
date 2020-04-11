function searcher(searchBarID,dataListID,urlString,parentHolderID,searchString){
    var searchBar = document.getElementById(searchBarID);
    var searchresultBar = document.createElement("datalist");
    resultArray = ["Firefox","Opera","chrome","Edger","Mozilla"];
    console.log("Hit from Inside JS","searchstring is",searchString);

    for (i=0;i<resultArray.length;i++){
        var option = document.createElement("option");
        option.value = resultArray[i];
        searchresultBar.appendChild(option);

    }
    //console.log(searchresultBar);
    var abcd = document.getElementById(parentHolderID);
    var rb = document.getElementById(dataListID);
    searchresultBar.setAttribute("id",dataListID);
    abcd.replaceChild(searchresultBar,rb);
}

// searchBar id, dataList id, URL String, Search String
