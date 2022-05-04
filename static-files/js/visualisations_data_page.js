import {
  forceSimulation,
  forceManyBody,
  forceLink,
  forceCenter,
} from 'https://cdn.skypack.dev/d3-force@3';

let svg = d3.select('#data-vis-container');

const width = +svg.attr('width');
const height = +svg.attr('height');

svg.attr("viewBox", "0 0 " + width + " " + height )
  .attr("preserveAspectRatio", "xMinYMin");

const centerX = width / 2;
const centerY = height / 2;

const nodeRadius = 6;

var nodeColor = d3.scaleOrdinal(d3.schemeSet3);
var gapLinkColorOrange = 'rgba(255,127,1,255)'; // color for GAP-type links
var synLinkColorBlue = 'rgba(23,118,182,255)'; // color for SYN-type links


d3.json(dataFile).then(function (data) {

  const simulation = forceSimulation()
    .nodes(data.nodes)
    .force('charge', forceManyBody().strength(-40))
    .force('link', forceLink(data.links).id((d) => d.id))
    .force('center', forceCenter(centerX, centerY))
    .force('forceX', d3.forceX(-1))  // keeps the unconnected nodes together with the rest on a screen
    .force('forceY', d3.forceY(-1))  // keeps the unconnected nodes together with the rest on a screen
    .force('collide', d3.forceCollide(10));
  
  // node tooltip
  const nodeTooltip = d3
    .select('#data-vis-wrapper')
    .append('div')
    .style('visibility', 'hidden')
    .attr('class', 'tooltip');

  const tooltipIn = function (event, d) {
    return nodeTooltip
      .html(
        '<h3>Neuron name:</h3>' + '<span>' + d.id + '</span>' + 
        '<h3>Neuron class:</h3>' + '<span>' + d.className + '</span>'
      )
      .style('visibility', 'visible') 
      .style('top', event.pageY + 'px') 
      .style('left', event.pageX + 'px')
  }

  const tooltipOut = function() {
    return nodeTooltip
      .transition()
      .duration(50)
      .style('visibility', 'hidden')
  }

  const link = svg
    .selectAll('line')
    .data(data.links)
    .enter()
    .append('line')
    .attr('opacity', 0.3)
    .style('stroke', function (d) {
      if (d.edgeTypeName === 'syn') {
        return synLinkColorBlue; // syn link
      } else {
        return gapLinkColorOrange; // gap link
      }
    })
    .attr('stroke-width', function (d) { return Math.sqrt(d.numOfEdges); });
  
  const node = svg
    .attr('class', 'nodes')
    .selectAll('circles')
    .data(data.nodes)
    .enter()
    .append('circle')
    .attr('r', nodeRadius)
    .style('stroke', 'black')
    .style('stroke-width', .5)
    .attr('fill', function (d) { return nodeColor(d.className); })
    .on('mouseover', tooltipIn)
    .on('mouseout', tooltipOut)
    .call(nodeDragging(simulation));
  
  simulation.on('tick', ticked);

  function ticked() {

    node
      // .attr('cx', (nd) => nd.x) // nd => node
      // .attr('cy', (nd) => nd.y);
      // this two lines of code below keep all nodes within the boundaries of the vis container even when dragged
      .attr('cx', function(nd) { return nd.x = Math.max(nodeRadius, Math.min(width - nodeRadius, nd.x)); })
      .attr('cy', function(nd) { return nd.y = Math.max(nodeRadius, Math.min(height - nodeRadius, nd.y)); }); 
  
    link
      .attr('x1', (lk) => lk.source.x) // lk => link
      .attr('y1', (lk) => lk.source.y)
      .attr('x2', (lk) => lk.target.x)
      .attr('y2', (lk) => lk.target.y);
  };

  // Code from observable, all credits to d3js-team. Source: https://observablehq.com/@d3/zoom
  // visualisation zooming
  // svg.call(d3.zoom()
  //     .extent([[0, 0], [width, height]])
  //     .scaleExtent([0, 8])
  //     .on('zoom', zoomed));

  // function zoomed({transform}) {
  //   node.attr('transform', transform);
  //   link.attr('transform', transform);
  // };

  return svg.canvas;

}).catch((err) => alert(err.message));

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
    .on('start', dragStarted)
    .on('drag', dragged)
    .on('end', dragEnded);
};