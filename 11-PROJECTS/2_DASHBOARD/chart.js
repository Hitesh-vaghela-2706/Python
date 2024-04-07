function PieChart() {
    $.get("csv/1pie.csv", function(csvString) {
       // transform the CSV string into a 2-dimensional array
       var arrayData = $.csv.toArrays(csvString, {onParseValue: $.csv.hooks.castToScalar});
 
       // this new DataTable object holds all the data
       var data = new google.visualization.arrayToDataTable(arrayData);
       // CAPACITY - En-route ATFM delay - YY - CHART
       var crt_ertdlyYY = new google.visualization.ChartWrapper({
          chartType: 'PieChart',
          containerId: 'graph1',
          dataTable: data,
          options:{
             title: 'Enrollment By Cource',
             titleTextStyle : {color: 'gray', fontSize: 16},
          }
       });
       crt_ertdlyYY.draw();
    });
 }
 google.setOnLoadCallback(PieChart)


//  barchart

function BarChart() {
    $.get("csv/2bar.csv", function(csvString) {
       // transform the CSV string into a 2-dimensional array
       var arrayData = $.csv.toArrays(csvString, {onParseValue: $.csv.hooks.castToScalar});
 
       // this new DataTable object holds all the data
       var data = new google.visualization.arrayToDataTable(arrayData);
       // CAPACITY - En-route ATFM delay - YY - CHART
       var crt_ertdlyYY = new google.visualization.ChartWrapper({
          chartType: 'BarChart',
          containerId: 'graph2',
          dataTable: data,
          options:{
             
             title: 'Enrollment By Ethencity',
             pieHole:0.4,
             titleTextStyle : {color: 'gray', fontSize: 16},
          }
       });
       crt_ertdlyYY.draw();
    });
 }
 google.setOnLoadCallback(BarChart)


//  histogram

function HistoGram() {
    $.get("csv/3hist.csv", function(csvString) {
       // transform the CSV string into a 2-dimensional array
       var arrayData = $.csv.toArrays(csvString, {onParseValue: $.csv.hooks.castToScalar});
 
       // this new DataTable object holds all the data
       var data = new google.visualization.arrayToDataTable(arrayData);
       // CAPACITY - En-route ATFM delay - YY - CHART
       var crt_ertdlyYY = new google.visualization.ChartWrapper({
          chartType: 'Histogram',
          containerId: 'graph3',
          dataTable: data,
          options:{
            
             title: 'Enrollment By Age',
             titleTextStyle : {color: 'gray', fontSize: 16},
          }
       });
       crt_ertdlyYY.draw();
    });
 }
 google.setOnLoadCallback(HistoGram)


//  combochart

function ComboChart() {
    $.get("csv/4combo.csv", function(csvString) {
       // transform the CSV string into a 2-dimensional array
       var arrayData = $.csv.toArrays(csvString, {onParseValue: $.csv.hooks.castToScalar});
 
       // this new DataTable object holds all the data
       var data = new google.visualization.arrayToDataTable(arrayData);
       // CAPACITY - En-route ATFM delay - YY - CHART
       var crt_ertdlyYY = new google.visualization.ChartWrapper({
          chartType: 'ComboChart',
          containerId: 'graph4',
          dataTable: data,
          options:{
            
             title: 'University Comparision By Ranking',
             seriesType: 'bars',
             titleTextStyle : {color: 'gray', fontSize: 16},
          }
       });
       crt_ertdlyYY.draw();
    });
 }
 google.setOnLoadCallback(ComboChart)


function GeoCHart() {
   $.get("csv/5geo.csv", function(csvString) {
      // transform the CSV string into a 2-dimensional array
      var arrayData = $.csv.toArrays(csvString, {onParseValue: $.csv.hooks.castToScalar});

      // this new DataTable object holds all the data
      var data = new google.visualization.arrayToDataTable(arrayData);
      // CAPACITY - En-route ATFM delay - YY - CHART
      var crt_ertdlyYY = new google.visualization.ChartWrapper({
         chartType: 'GeoChart',
         containerId: 'graph5',
         dataTable: data,
         options:{
            title: 'Universities Per Country',
            titleTextStyle : {color: 'gray', fontSize: 16},
         }
      });
      crt_ertdlyYY.draw();
   });
}
google.setOnLoadCallback(GeoCHart)

//  areachart

function AreaChart() {
    $.get("csv/6area.csv", function(csvString) {
       // transform the CSV string into a 2-dimensional array
       var arrayData = $.csv.toArrays(csvString, {onParseValue: $.csv.hooks.castToScalar});
 
       // this new DataTable object holds all the data
       var data = new google.visualization.arrayToDataTable(arrayData);
       // CAPACITY - En-route ATFM delay - YY - CHART
       var crt_ertdlyYY = new google.visualization.ChartWrapper({
          chartType: 'AreaChart',
          containerId: 'graph6',
          dataTable: data,
          options:{
             
             title: 'Admission Per Year',
             titleTextStyle : {color: 'gray', fontSize: 16},
          }
       });
       crt_ertdlyYY.draw();
    });
 }
 google.setOnLoadCallback(AreaChart)

//  donutcahart

function donutcahart() {
    $.get("csv/7donut.csv", function(csvString) {
       // transform the CSV string into a 2-dimensional array
       var arrayData = $.csv.toArrays(csvString, {onParseValue: $.csv.hooks.castToScalar});
 
       // this new DataTable object holds all the data
       var data = new google.visualization.arrayToDataTable(arrayData);
       // CAPACITY - En-route ATFM delay - YY - CHART
       var crt_ertdlyYY = new google.visualization.ChartWrapper({
          chartType: 'PieChart',
          containerId: 'graph7',
          dataTable: data,
          options:{
            
             title: 'Enrollment By Gender ',
             pieHole:0.4,
             titleTextStyle : {color: 'gray', fontSize: 16},
          }
       });
       crt_ertdlyYY.draw();
    });
 }
 google.setOnLoadCallback(donutcahart)

//  linechart

function LineChart() {
    $.get("csv/8line.csv", function(csvString) {
       // transform the CSV string into a 2-dimensional array
       var arrayData = $.csv.toArrays(csvString, {onParseValue: $.csv.hooks.castToScalar});
 
       // this new DataTable object holds all the data
       var data = new google.visualization.arrayToDataTable(arrayData);
       // CAPACITY - En-route ATFM delay - YY - CHART
       var crt_ertdlyYY = new google.visualization.ChartWrapper({
          chartType: 'LineChart',
          containerId: 'graph8',
          dataTable: data,
          options:{
            
             title: 'Administrative Spending Per Student',
             titleTextStyle : {color: 'gray', fontSize: 16},
          }
       });
       crt_ertdlyYY.draw();
    });
 }
 google.setOnLoadCallback(LineChart)


//  top-5 collages

function drawVisualization() {
    $.get("csv/9pie.csv", function(csvString) {
       // transform the CSV string into a 2-dimensional array
       var arrayData = $.csv.toArrays(csvString, {onParseValue: $.csv.hooks.castToScalar});
 
       // this new DataTable object holds all the data
       var data = new google.visualization.arrayToDataTable(arrayData);
       // CAPACITY - En-route ATFM delay - YY - CHART
       var crt_ertdlyYY = new google.visualization.ChartWrapper({
          chartType: 'PieChart',
          containerId: 'graph9',
          dataTable: data,
          options:{
            
             title: 'Top Collages By Applications',
             titleTextStyle : {color: 'gray', fontSize: 16},
          }
       });
       crt_ertdlyYY.draw();
    });
 }
 google.setOnLoadCallback(drawVisualization)


//  candalistic chart

function CandalisticCHart() {
   $.get("csv/10candle.csv", function(csvString) {
      // transform the CSV string into a 2-dimensional array
      var arrayData = $.csv.toArrays(csvString, {onParseValue: $.csv.hooks.castToScalar});

      // this new DataTable object holds all the data
      var data = new google.visualization.arrayToDataTable(arrayData);
      // CAPACITY - En-route ATFM delay - YY - CHART
      var crt_ertdlyYY = new google.visualization.ChartWrapper({
         chartType: 'CandlestickChart',
         containerId: 'graph10',
         dataTable: data,
         options:{
            title: 'Universities Performance By Exams',
            titleTextStyle : {color: 'gray', fontSize: 16},
         }
      });
      crt_ertdlyYY.draw();
   });
}
google.setOnLoadCallback(CandalisticCHart)