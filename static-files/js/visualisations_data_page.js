Promise.all([
  d3.csv(edgesDataFile),
  d3.csv(classesDataFile),
  d3.csv(neuronsDataFile),
  d3.csv(connectomesDataFile),
  // d3.json(nodesDataFile),
  // d3.json(linksDataFile)
]).then(function(files) {
  console.log(files[0]);
  console.log(files[1]);
  console.log(files[2]);
  console.log(files[3]);
  // console.log(files[4]);
  // console.log(files[5]);
});