import {
  forceSimulation,
  forceManyBody,
  forceLink,
  forceCenter
} from "https://cdn.skypack.dev/d3-force@3";



// Promise.all([
  // d3.csv(edgesDataFile),
  // d3.csv(classesDataFile),
  // d3.csv(neuronsDataFile),
  // d3.csv(connectomesDataFile),
  // d3.json(nodesDataFile),
  // d3.json(linksDataFile),
//   d3.json(dataFile)
// ]).then(function(files) {
//   console.log(files[0]);
  // console.log(files[1]);
  // console.log(files[2]);
  // console.log(files[3]);
  // console.log(files[4]);
  // console.log(files[5]);
  // console.log(files[6]);
// });

let svg = d3.select('#data-vis-container');

const width = +svg.attr('width');
const height = +svg.attr('height');

const centerX = width / 2;
const centerY = height / 2;

d3.json(dataFile).then(function(data) {
  const n = data; // nodes
  console.log(n.nodes);
  const l = data; // links
  console.log(l.links);

  const simulation = forceSimulation(n)
    .force('charge', forceManyBody())
    .force('link', forceLink(l))
    .force('center', forceCenter(centerX, centerY));
});

// const nodes = [
//   {id: dataFile.neuronName}
// ];

// console.log(nodes);

// const links = [
//   {source: dataFile.sourceNeuron, target: dataFile.targetNeuron}
// ];

// console.log(links);

// let svg = d3.select('#data-vis-container');

// const width = +svg.attr('width');
// const height = +svg.attr('height');

// const centerX = width / 2;
// const centerY = height / 2;

// const simulation = forceSimulation(nodes)
//   .force('charge', forceManyBody())
//   .force('link', forceLink(links).id((d) => {return d.id}))
//   .force('center', forceCenter(centerX, centerY));

// const circles = svg
//   .selectAll('circle')
//   .data(nodes)
//   .enter()
//   .append('circle')
//   .attr('r', 20);

// simulation.on('tick', () => {
//   circles
//     .attr('cx', d => {d.x})
//     .attr('cy', d => {d.y});
// });