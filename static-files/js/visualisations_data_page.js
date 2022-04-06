import {
  forceSimulation,
  forceManyBody,
  forceLink,
  forceCenter,
} from 'https://cdn.skypack.dev/d3-force@3';



let svg = d3.select('#data-vis-container');

const width = +svg.attr('width');
const height = +svg.attr('height');

const centerX = width / 2;
const centerY = height / 2;

var nodeColor = d3.scaleOrdinal(d3.schemeSet3);
var linkColor = d3.scaleOrdinal(d3.schemeCategory10);

d3.json(dataFile).then(function (data) {
  // if (error) throw error;

  const simulation = forceSimulation()
    .nodes(data.nodes)
    .force('charge', forceManyBody().strength(-40))
    .force('link', forceLink(data.links).id((d) => d.id))
    .force('center', forceCenter(centerX, centerY))
    .force('forceX', d3.forceX(-1))  // keeps the unconnected nodes together with the rest
    .force('forceY', d3.forceY(-1)); // keeps the unconnected nodes together with the rest

  const link = svg
    .selectAll('line')
    .data(data.links)
    .enter()
    .append('line')
    .attr('opacity', 0.3)
    .style('stroke', function(d){ return linkColor(d.edgeTypeName) })
    .attr('stroke-width', function(d) { return Math.sqrt(d.numOfEdges); });
  
  const node = svg
    .attr('class', 'nodes')
    .selectAll('circles')
    .data(data.nodes)
    .enter()
    .append('circle')
    .attr('r', 5)
    .style("stroke", "black")
    .style("stroke-width", .5)
    .attr("fill", function (d) { return nodeColor(d.className); })
    .call(nodeDragging(simulation));

  simulation.on('tick', ticked);

  function ticked() {
    link
      .attr('x1', (lk) => lk.source.x) // lk => link
      .attr('y1', (lk) => lk.source.y)
      .attr('x2', (lk) => lk.target.x)
      .attr('y2', (lk) => lk.target.y);

    node
      .attr('cx', (nd) => nd.x) // nd => node
      .attr('cy', (nd) => nd.y);
  }

  // Code from observable, all credits to d3js-team. Source: https://observablehq.com/@d3/zoom
  // visualisation zooming
  svg.call(d3.zoom()
      .extent([[0, 0], [width, height]])
      .scaleExtent([0, 8])
      .on("zoom", zoomed));

  function zoomed({transform}) {
    node.attr("transform", transform);
    link.attr("transform", transform);
  }
});

// Code from observable, all credits to d3js-team. Source: https://observablehq.com/@d3/force-directed-graph
// node dragging 
function nodeDragging(simulation) {    
  function dragStarted(event) {
    if (!event.active) simulation.alphaTarget(0.3).restart();
    event.subject.fx = event.subject.x;
    event.subject.fy = event.subject.y;
  }
  
  function dragged(event) {
    event.subject.fx = event.x;
    event.subject.fy = event.y;
  }
  
  function dragEnded(event) {
    if (!event.active) simulation.alphaTarget(0);
    event.subject.fx = null;
    event.subject.fy = null;
  }
  
  return d3.drag()
    .on("start", dragStarted)
    .on("drag", dragged)
    .on("end", dragEnded);
}